import os
import tornado.web
import tornado.gen
import tornado.httpclient


class DownLoad(tornado.web.RequestHandler):

    def get(self):
        self.render('download.html')

    def post(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 拼接出直接路径
        file = self.get_argument('filename', '')
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename={}'.format(file))
        path = os.path.join(BASE_DIR, 'data', file)

        def down(size=512):
            """
            下载器
            :param size:
            :return:
            """
            with open(path, 'rb') as f:
                while True:
                    result = f.read(size)
                    if result:
                        self.write(result)

                    else:
                        break

        down()
        self.finish()








'''
def post():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 拼接出直接路径
    file = self.get_argument('filename', '')
    self.set_header('Content-Type', 'application/octet-stream')
    self.set_header('Content-Disposition', 'attachment; filename={}'.format(file))
    path = os.path.join(BASE_DIR, 'data', file)

    def down(size=512):
        """
        下载器
        :param size:
        :return:
        """
        with open(path, 'rb') as f:
            while True:
                result = f.read(size)
                if result:
                    self.write(result)

                else:
                    break

    down()
    self.finish()
'''

