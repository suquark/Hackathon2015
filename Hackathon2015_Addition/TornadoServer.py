__author__ = 'suquark'
import os
import tornado
from tornado.ioloop import IOLoop
import tornado.web
from tornado.web import RequestHandler, Application, authenticated
import win32api
import win32con
import time

class GetUserHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(GetUserHandler):
    @authenticated
    def get(self):
        # self.write("Hello, world")
        self.render('panel.html')
#IP=self.request.remote_ip
# self.request.headers['X-Real-Ip']

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

        
class kbdctl(RequestHandler):
    def get(self):
        key=int(self.get_argument('key'))
        win32api.keybd_event(key,0,0,0)
        time.sleep(0.2)
        win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
        
class kbdctl2(RequestHandler):
    def get(self):
        key1 = int(self.get_argument('key1'))
        key2 = int(self.get_argument('key2'))  
        win32api.keybd_event(key1,0,0,0)
        win32api.keybd_event(key2,0,0,0)
        time.sleep(0.2)
        win32api.keybd_event(key2,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(key1,0,win32con.KEYEVENTF_KEYUP,0)

    
class sysctl(RequestHandler):
    def get(self):
        cmd=self.get_argument('cmd')
        os.system(cmd)
 
class prexss(RequestHandler):
    def get(self):
        self.render("xssform.html")


class xss(RequestHandler):
    def post(self):
        self.write("<html><h1>%s</h1></html>" % self.get_argument('uid'))

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
    (r'/kbdctl', kbdctl),
    (r'/sysctl', sysctl),
    (r'/kbdctl2', kbdctl2),
    (r'/prexss', prexss),
    (r'/xss', xss),
], **settings)


if __name__ == "__main__":
    application.listen(80)
    IOLoop.instance().start()
    
"""
ESC键 VK_ESCAPE (27)
回车键： VK_RETURN (13)
TAB键： VK_TAB (9)
Caps Lock键： VK_CAPITAL (20)
Shift键： VK_SHIFT ($10)
Ctrl键： VK_CONTROL (17)
Alt键： VK_MENU (18)
空格键： VK_SPACE ($20/32)
退格键： VK_BACK (8)
左徽标键： VK_LWIN (91)
右徽标键： VK_LWIN (92)
鼠标右键快捷键：VK_APPS (93)
Insert键： VK_INSERT (45)
Home键： VK_HOME (36)
Page Up： VK_PRIOR (33)
PageDown： VK_NEXT (34)
End键： VK_END (35)
Delete键： VK_DELETE (46)

方向键(←)： VK_LEFT (37)

方向键(↑)： VK_UP (38)

方向键(→)： VK_RIGHT (39)

方向键(↓)： VK_DOWN (40)

F1键： VK_F1 (112)

F2键： VK_F2 (113)

F3键： VK_F3 (114)

F4键： VK_F4 (115)

F5键： VK_F5 (116)

F6键： VK_F6 (117)

F7键： VK_F7 (118)

F8键： VK_F8 (119)

F9键： VK_F9 (120)

F10键： VK_F10 (121)

F11键： VK_F11 (122)

F12键： VK_F12 (123)

Num Lock键： VK_NUMLOCK (144)

小键盘0： VK_NUMPAD0 (96)

小键盘1： VK_NUMPAD0 (97)

小键盘2： VK_NUMPAD0 (98)

小键盘3： VK_NUMPAD0 (99)

小键盘4： VK_NUMPAD0 (100)

小键盘5： VK_NUMPAD0 (101)

小键盘6： VK_NUMPAD0 (102)

小键盘7： VK_NUMPAD0 (103)

小键盘8： VK_NUMPAD0 (104)

小键盘9： VK_NUMPAD0 (105)

小键盘.： VK_DECIMAL (110)

小键盘*： VK_MULTIPLY (106)

小键盘+： VK_MULTIPLY (107)

小键盘-： VK_SUBTRACT (109)

小键盘/： VK_DIVIDE (111)

Pause Break键： VK_PAUSE (19)

Scroll Lock键： VK_SCROLL (145)
"""
