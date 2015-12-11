#!/usr/bin/env python
# coding:utf8
import web

render = web.template.render('tpl/')  # 定义网页模板对象,用于网页渲染
db = web.database(dbn='mysql', user='tdo', pw='tdo', db='tdo')  # 创建数据对象,用于操作数据

urls = (
    '/', 'index',
    '/add', 'add'
)


class index:
    def GET(self):
        # i = web.input(name=None) #web.input接受客户端所有的输入数据,包括form和url传参过来的
        # return render.index(name) #此处的index是指的模板目录tpl下的index.html

        tdos = db.select('todo')
        return render.index(tdos)


class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)  # 此处声明的变量n用于保存插入数据的行号,如果不需要返回也可以不用定义声明变量.
        raise web.seeother('/')               # db.insert('todo',title=i.title) 这样也行


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

