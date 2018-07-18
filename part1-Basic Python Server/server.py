from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#Start by importing myHandler Class from requestHandler.py file

#Every server needs to listen on a port with a unique number. The
#standard port for HTTP servers is port 8000,
PORT_NUMBER = 8080

try:
	#This statement creates a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), 'Fill_Me_In')
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()