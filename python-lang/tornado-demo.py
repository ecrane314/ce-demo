"""
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O,
Tornado can scale to tens of thousands of open connections, making it ideal
for long polling, WebSockets, and other applications that require a long-lived
connection to each user.
https://www.tornadoweb.org/en/stable/
"""

import tornado.web
import tornado.ioloop

# Override RequestHandler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")


class IconHandler(tornado.web.StaticFileHandler):
    def get(self):
        self.get_content(path="/Users/evancrane/Downloads/favicon.ico")
        #TODO BROKEN Should this be a configuration instead of a handler class?
        # https://www.tornadoweb.org/en/stable/_modules/tornado/web.html?highlight=favicon#

# Function to construct App that uses Handler
def make_app():
    # Call Application constructor with list of tuples
    # where each is a route and it's handler
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/favicon.ico", IconHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5050)
    tornado.ioloop.IOLoop.current().start()
