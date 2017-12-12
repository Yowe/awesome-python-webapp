# coding=utf-8

import os


dirpath = os.path.join('D:/test/', '你好'.decode('utf-8'))

print dirpath
os.makedirs(dirpath)