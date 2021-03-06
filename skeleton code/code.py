#!/usr/bin/env python
# coding: utf-8

import web

import view
from view import render

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return render.base(view.listing())


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
