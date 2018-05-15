# -*- coding: utf-8 -*-

import sys
sys.path.append('/root/work_venv/Testing/DZ_4/HW_4')

from wsgi_framework.otus import Otus

app = Otus()


@app.route('/')
def handler_1():
    return b'Main menu'


@app.route('/contacts/')
def handler_2():
    return b'Moscow, Web_dev street, 201'


def application(environ, start_response):
    return app.application(environ, start_response)
