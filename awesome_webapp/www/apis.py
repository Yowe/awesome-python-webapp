#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Yowe'

'''
json api definetion
'''

import json,logging,inspect,functools

class ApiError(Exception):
    def __init__(self, error, data='', message=''):
        super(ApiError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class ApiValueError(Exception):
    def __init__(self, field, message=''):
        super(ApiValueError, self).__init__('value:invalid', field, message)

class ApiResourceNotFoundError(ApiError):
    def __init__(self, field, message=''):
        super(ApiResourceNotFoundError, self).__init__('value:not found', data=field, message=message)

class APIPermissionError(ApiError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)


