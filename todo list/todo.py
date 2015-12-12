#!/usr/bin/env python
# coding: utf-8

"""base todo list using web.py 0.3"""

import web
import model

# url mappings
urls = (
    '/', 'index',
    'del/(\d+)', 'delete'
)


# templates
render = web.template.render('tpls/', base='base')


'''todo classes'''

class index:
    # 实例化web.form类，用于网页呈现
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, description='I need to:'),
        web.form.Button('Add todo'),
    )

    # 定义GET方法获取网页
    def GET(self):
        '''Show page'''
        todos = model.get_todos()  # 通过model类的get_todos方法获取数据
        form = self.form()  # 引用前面实例化的form对象
        return render.index(todos, form)  # 将两个变量渲染到模版index网页中

    # 定义POST方法将页面上输入的数据写入数据库
    def POST(self):
        '''Add new netry'''
        form = self.form()
        if not form.validates():  # 判断输入是否合法
            todos = model.get_todos()  # 如果输入不合法，将继续显示现有网页并由验证模块给出错误提示
            return render.index(todos, form)  #
        model.new_todo(form.d.title)  # 合法即调用new_todo方法将数据写入数据库
        raise web.seeother('/')  # raise 关键字用于自定义异常处理，这里的作用是：不管怎样都将调用web.seeother('/')对页面进行跳转


class delete:
    '''delete a todo'''

    def POST(self, id):  # 定义POST方法，接收一个参数传入，此参数是从web.input过来
        '''DELETE BASED ON ID'''
        id = int(id)  # 做数据类型转换是为了是传递过来的参数和数据库里的类型相符合
        model.del_todo(id)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
