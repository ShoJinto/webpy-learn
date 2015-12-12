#!/usr/bin/env python
# coding: utf-8
import web
import db
import config

t_globals = dict(datestr=web.datestr) #记得查查web.datestr具体什么意思

render = web.template.render('tpls/', cache=config.cache, globals=t_globals)
render._keywords['globals']['render'] = render


def listing(**k):
    l = db.listing(**k)
    return render.listing(l)
