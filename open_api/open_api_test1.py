import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """get请求"""
        a = self.get_argument('a')
        b = self.get_argument('b')
        c = int(a) + int(b)

        self.write("c=" + str(c))


application = tornado.web.Application([(r"/xuyz", MainHandler), ])

if __name__ == "__main__":
    application.listen(8868)  # 设置监听
    tornado.ioloop.IOLoop.instance().start()
