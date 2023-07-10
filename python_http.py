import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 9000


class WebRequestsHandler(BaseHTTPRequestHandler):

    def set_headers(self, type):
        self.send_response(200)
        self.send_header("Content-Type", type)
        self.end_headers()

    def do_GET(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        data = response.json()
        self.set_headers('application/json')
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def do_POST(self):
        api_url = "https://jsonplaceholder.typicode.com/posts"
        new_post = {
            "userId": 10,
            "id": 10,
            "title": "Python practice",
            "body": "Hello, I am Maryam. Nice to meet you!"
        }
        response = requests.post(api_url, json=new_post)
        data = response.json()
        self.set_headers('application/json')
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def do_PUT(self):
        api_url = "https://jsonplaceholder.typicode.com/posts/1"
        update_post = {
            "userId": 1,
            "id": 1,
            "title": "The Art of War",
            "body": "An ancient Chinese military "
            "text written by Sun Tzu."
        }
        response = requests.put(api_url, json=update_post)
        data = response.json()
        self.set_headers('application/json')
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def do_PATCH(self):
        api_url = "https://jsonplaceholder.typicode.com/posts/1"
        patch_post = {
            "title": "The Odyseey"
        }
        response = requests.patch(api_url, patch_post)
        data = response.json()
        self.set_headers('application/json')
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def do_DELETE(self):
        response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
        data = response.json()
        self.set_headers('application/json')
        self.wfile.write(bytes(json.dumps(data)), "utf-8")


server = HTTPServer((HOST, PORT), WebRequestsHandler)
print("Server Now Running...")
server.serve_forever()

