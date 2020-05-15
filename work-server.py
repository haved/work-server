#!/usr/bin/env python3

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from os import getenv

HOST = ""
PORT = int(getenv("PORT", "8000"))

HTML_MIME = "text/html"

def read_file(filename):
    with open(filename) as f:
        return f.read()

class RequestHandler(BaseHTTPRequestHandler):
    def output_file(self, filename, content_type):
        self.output(read_file(filename).encode('utf-8'), f"{content_type}; charset=UTF-8")

    def output(self, bytedata, content_type):
        self.send_response(200, 'OK')
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(bytedata))
        self.end_headers()
        self.wfile.write(bytedata)

    def redirect(self, to):
        self.send_response(301)
        self.send_header('Location', to)
        self.end_headers()

    def do_GET(self):
        self.protocol_version = 'HTTP/1.1'
        if self.path == "/" or self.path == "/index.html":
            self.output_file("public/index.html", HTML_MIME)
        else:
            self.output_file("public/404.html", HTML_MIME)

    def do_POST(self):
        pass

def main():
    with ThreadingHTTPServer((HOST,PORT), RequestHandler) as httpd:
        print(f"Serving work server on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
