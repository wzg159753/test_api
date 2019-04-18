import tornado.web


class DownLoad(tornado.web.RequestHandler):

    def get(self):
        self.write('hello world')

    def post(self):
        pass