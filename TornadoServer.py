__author__ = 'suquark'
import os
import tornado
import oxfordcv
import picamera
from tornado.ioloop import IOLoop
import tornado.web
from tornado.web import RequestHandler, Application, authenticated
import json


class GetUserHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(GetUserHandler):
    @authenticated
    def get(self):
        # self.write("Hello, world")
        self.render('panel.html')


class LoginHandler(RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        self.set_secure_cookie("user", self.get_argument('name'))
        self.redirect('/')


class NewPageHandler(RequestHandler):
    def get(self):
        self.write('<script>alert('');</script>')
        self.redirect('/login')


imgpath = ''
info = ''


class Refrigerator_Opened(RequestHandler):
    def get(self):
        print('Server: Set Path')
        globals()['imgpath'] = '/static/' + os.path.basename(self.get_argument('path'))
        globals()['info'] = json.dumps(self.get_argument('info'))


class polling(RequestHandler):
    def get(self):
        self.write(globals()['info'])
        globals()['info'] = ''

class image(RequestHandler):
    def get(self):
        pt = globals()['imgpath']
        globals()['imgpath'] = ''
        self.redirect(pt)


class OCRHandler(RequestHandler):
    def get(self):
        camera = picamera.PiCamera()
        camera.video_stabilization = True
        print('Capturing picture...')
        camera.capture('temp.jpg')
        camera.close()
        print('Analyzing...')
        self.write(oxfordcv.ocr('temp.jpg', 'en'))


settings = {
    "cookie_secret": "udhdchguygG^&*Y%76798UH&*GfD%^&TG%^$D^%&TXg*(YG7xf677",
    "login_url": "/login",
    "xsrf_cookies": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/newpage", NewPageHandler),
    (r"/ocr", OCRHandler),
    (r"/Refrigerator_Opened", Refrigerator_Opened),
    (r"image", image),
    (r"/poll", polling),

], **settings)

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()
