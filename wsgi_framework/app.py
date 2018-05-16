# -*- coding: utf-8 -*-

import sys
# Костыль для корректного импортирования
sys.path.append('/root/work_venv/Testing/DZ_4/HW_4')
from wsgi_framework.otus import Otus

app = Otus()


@app.route('/')
def handler_1():
    return 'Main menu'


@app.route('/contacts/')
def handler_2():
    return 'Moscow city, Web developers st., 418'


def application(environ, start_response):
    return app.application(environ, start_response)
