#!usr/bin/python
# -*- coding: utf-8 -*-

__author__='Yowe'
import asyncio,os,inspect,logging,functools
from urllib import parse
from aiohttp import web
from apis import ApiError

def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
        
