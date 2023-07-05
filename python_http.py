from http.server import HTTPServer,BaseHTTPRequestHandler

PORT=8080
HOST="127.0.0.1"

class WebRequestsHandler(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(200)
        self.send_header("Content Type","text/html")
        self.end_headers()

    def do_GET(self):
        self.wfile.write(bytes("<html><body><h1>GET method</h1></body></html>","utf-8"))

    def do_POST(self):
        self.wfile.write(bytes("<html><body><h1>POST method</h1></body></html>","utf-8"))


server=HTTPServer((HOST,PORT), WebRequestsHandler)
print("server now running")
server.serve_forever()