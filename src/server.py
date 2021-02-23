
import tornado.ioloop
import tornado.web
import settings
from handlers.landing import MainHandler
# Create the application before creating a MotorClient.
application = tornado.web.Application([
    (r'/', MainHandler)
])

server = tornado.httpserver.HTTPServer(application)
server.bind(8888)

# Forks one process per CPU.
server.start(0)

# Now, in each child process, create a MotorClient.
application.settings['db'] = settings.mongo_client.pos
tornado.ioloop.IOLoop.current().start()
