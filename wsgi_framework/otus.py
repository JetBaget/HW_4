# -*- coding: utf-8 -*-

import json


class Otus:
    def __init__(self):
        self.routing = dict()
        self.env = None
        self.environ = None

    def route(self, url):
        def routed(f):
            stripped_url = url.rstrip('/') if url != '/' else url
            self.routing[stripped_url] = f
            return f
        return routed

    def parse_env(self, environ):
        self.env = dict(query=environ['QUERY_STRING'],
                        method=environ['REQUEST_METHOD'],
                        url=environ['PATH_INFO'],
                        host=environ['HTTP_HOST'],
                        port=environ['SERVER_PORT'],
                        address=environ['REMOTE_ADDR'])

    def application(self, environ, start_response):
        self.environ = environ
        self.parse_env(environ)
        url = self.env['url']
        if url.split('/')[-1] == 'environ':
            return json.dumps(self.env).encode('utf-8')
        start_response('200 OK', [('Content-Type', 'text/plain')])
        try:
            view = self.routing[url]
            status = '200'
            data = view()
        except KeyError:
            status = '404'
            data = None
        return json.dumps({'status': status, 'data': data}).encode('utf-8')
