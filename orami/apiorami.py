import orami
import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
 

class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    def html(self, message):
        content =  f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")
    

    def do_GET(self):
        try:
            parse= urlparse(self.path)
            path= parse.path
            
            # if path == "/help":
            #     self.send_response(200)

            
            result = orami.scrap(path)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(result.encode())
        except:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.html("Requested information is incomplete or malformed"))

        return
        

httpd = HTTPServer(('localhost', 8000), RestHTTPRequestHandler)


while True:
    httpd.handle_request()