from http.server import BaseHTTPRequestHandler,HTTPServer
import os
PORT_NUMBER = 5000
import subprocess
#This class will handles any incoming request from
#the browser#
import urllib.parse as urlparse
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        id = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('id', None)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        print(id)
        if id[0] == 'top':
            subprocess.run(["python", "--version", "&"])               
        self.wfile.write(bytes("Oh, Thanks Cronnie! I'm waked up! " + str(id[0]), "UTF-8"))

        return
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        subprocess.run(["python", "codalBot.py", "telegram", post_body, "&"])
        self.wfile.write(bytes("Oh, Thanks Cronnie! I'm waked up! ", "UTF-8") + post_body)
        return
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' , PORT_NUMBER)
    
    #Wait forever for incoming htto requests
    server.serve_forever()
    #server.handle_request()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
