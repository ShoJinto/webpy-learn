#!/usr/bin/env python
# coding: utf-8

import web

db = web.database(dbn='mysql', db='todo', user='todo', pw='todo')


def get_todos():
    return db.select('todo_v1', order='id')


def new_todo(text):
    db.insert('todo_v1', title=text)


def del_todo(id):
    db.delete('todo_v1', where="id=$id", vars=locals())

