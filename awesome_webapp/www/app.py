#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="Yowe"

'''
async web application
'''

import  logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app=web.application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

