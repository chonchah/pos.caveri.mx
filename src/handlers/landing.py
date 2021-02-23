
import tornado.web

from bson import json_util


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        db = self.settings['db']
        doc = db.productos.find()
        self.write(json_util.dumps(doc))
