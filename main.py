import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Some Changes")
class listRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

if __name__ == '__main__':
	app = tornado.web.Application([
		(r"/", basicRequestHandler),
		(r"/animal",listRequestHandler)
		])

	port = 8882
	app.listen(port)
	print(f"Application is ready and listen on port {port}")
	tornado.ioloop.IOLoop.current().start()
