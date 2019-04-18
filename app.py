import tornado.web
import tornado.ioloop
import tornado.options
from tornado.options import define, options

from handler import main


define(name='port', default=9090, help='run port', type=int)


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/download', main.DownLoad),
        ]

        settings = dict(
            debug = True,
            template_path = 'templates',
            static_path = 'static'
        )

        super().__init__(handlers, **settings)

app = Application()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()