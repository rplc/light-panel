from http.server import BaseHTTPRequestHandler, HTTPServer
#import lightpanel
from os import path, sep, system
import json
import threading

PORT_NUMBER = 8080
webPath = sep + '..' + sep + 'web'

def killAllLightpanels(server):	
	threading.Thread(target=server.shutdown, daemon=True).start()

	try:
		lightpanel.shutdown()
	except:
		pass

	system('systemctl poweroff')

class myHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		if self.path == "/":
			self.path = "/index.html"

		try:
			sendReply = False
			# Check the mimetype of the requested file
			if self.path.endswith(".html"):
				mimetype = 'text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype = 'image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype = 'image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype = 'application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype = 'text/css'
				sendReply = True
			if self.path.endswith(".ico"):
				mimetype = 'image/x-icon'
				sendReply = True
			if self.path.endswith(".png"):
				mimetype = 'image/png'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				filePath = path.dirname(path.abspath(__file__)) + webPath + self.path
				f = open(filePath, 'rb') 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	def do_POST(self):
		if self.path == '/api/setColor':
			content_length = int(self.headers['Content-Length'])
			data = self.rfile.read(content_length)
			data = data.decode('utf-8')

			if data == '' or self.headers['Content-Type'] != 'application/json':
				self.send_error(400, 'Empty data or not json.')
			else:
				parsed = json.loads(data)

				try:
					lightpanel.setColor(parsed['color'])

					self.send_response(200)
					self.end_headers()
				except:
					self.send_error(418, 'Some error while setting the color occured.')
		elif self.path == '/api/shutdown':
			print('Shutting the server down via api request')

			killAllLightpanels(server)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('Shutting the server down via ^C')
	killAllLightpanels(server)