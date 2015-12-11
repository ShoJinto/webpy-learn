#!/usr/bin/env python
# coding: utf-8

import web
from web import form

render = web.template.render('tpl/')

urls = (
    '/', 'index',
    '/login', 'login'
)

app = web.application(urls, globals())

myform = form.Form(
    form.Textbox('boe'),
    form.Textbox('bax',
                 form.notnull,
                 form.regexp('\d+', 'Must be a digit'),
                 form.Validator('Must be more than 5', lambda x: int(x) > 5)
                 ),
    form.Textarea('moe'),
    form.Checkbox('curly'),
    form.Dropdown('french', ['mustard', 'fries', 'wine'])
)

class login:
    login = form.Form(
        form.Textbox('username',
                     form.notnull),
        form.Password('password',
                      form.notnull,
                      form.Validator('The length is more than 6', lambda x: len(x) > 6)
                      ),
        form.Button('Login'))

    def GET(self):
        # lform = login()
        return render.login(self.login)


class index:
    def GET(self):
        form = myform()
        return render.formtest(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:
            return 'Grate success! boe: %s, bax: %s' % (form.d.boe, form['bax'].value)


if __name__ == '__main__':
    web.internalerror == web.debugerror
    app.run()
