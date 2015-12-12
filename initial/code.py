#!/usr/bin/env python
# coding: utf-8

import web

render = web.template.render('tpl/')  # 定义渲染模版在项目中的位置

db = web.database(dbn='mysql', user='tdo', pw='tdo', db='tdo')  # 创建数据对象，用于指定数据库类型，连接权限

urls = (
    "/", "index",
    "/add", "add"
)


# class index(object):
# 	"""docstring for index"""
# 	def  GET(self): #利用GET方式提供页面
# 		# return "Hello Webpy!"

# 		# name = 'ShoJinto'
# 		# return render.index(name)  #此处的index是指的模版中的index.html
# 		i = web.input(name=None)  #使用web.input方法用接收用户输入，即URL传参
# 		return render.index(i.name)  #访问形式 http://127.0.0.1/?name=shojinto

# class index(object):
# 	"""docstring for index"""
# 	def GET(self, name): # 定义GET方法接收URL参数传入
# 		return render.index(name) #访问形式 http://127.0.0.1/shojinto 

class index(object):
    """docstring for index"""

    def GET(self):
        tdos = db.select('tdo')
        return render.index(tdos)


class add(object):
    """docstring for add"""

    def POST(self):
        i = web.input()  # web.input 保存的时候form提交过来的所有数据
        n = db.insert('tdo', title=i.title)  # 其实这里可以不定义变量n 而直接执行db.insert()方法，该方法返回的是出入导数据后改行的行号
        # return render.n(i)
        raise web.seeother('/')


if __name__ == "__main__":  # 启动web服务
    app = web.application(urls, globals())
    app.run()
