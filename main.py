import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Some Changes")
        
class mainRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class listAPIRequestHandler(tornado.web.RequestHandler):
	def get(self):
		fh = open('list.txt', "r")
		lists = fh.read().splitlines()
		fh.close()
		self.write(json.dumps(lists))
	def post(self):
		fruit = self.get_argument("fruit")
		fh = open("list.txt", "a")
		fh.write(f"{fruit}\n")
		fh.close()
		self.write(json.dumps({"message" :"Fruit added"}))
class listRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class queryRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")

class resourceParamRequestHandler(tornado.web.RequestHandler):
	def get(self,studentName, courseId):
		self.write(f"Welcome {studentName}  the course you are viewing is {courseId}")

if __name__ == '__main__':
	app = tornado.web.Application([
		(r"/", basicRequestHandler),
        (r"/main", mainRequestHandler), 
		(r"/api", listAPIRequestHandler),
		(r"/animal",listRequestHandler),
        (r"/isEven", queryRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler)
		])
        
	port = 8081
	app.listen(port)
	print(f"Application is ready and listen on port {port}")
	tornado.ioloop.IOLoop.current().start()
