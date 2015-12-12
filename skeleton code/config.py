#!/usr/bin/env python
# coding:utf8

import web

db = web.database(dbn='mysql', db='apps', user='app', pw='app')
cache = False
