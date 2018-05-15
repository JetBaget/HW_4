# -*- coding: utf-8 -*-


class Otus:
    def __init__(self):
        self.routing = dict()

    def route(self, url):
        def routed(f):
            self.routing[url] = f
            return f
        return routed

    def application(self, environ, start_response):
        url = environ['PATH_INFO']
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [self.routing[url]()]
