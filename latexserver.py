#!/usr/bin/env python3

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HOST = ""
PORT = int(getenv("PORT", "80"))

def read_file(filename):
    with open(filename) as f:
        return f.read()

class LatexRequest(BaseHTTPRequestHandler):
    def output(bytedata, content_type):
        self.protocol_version = 'HTTP/2'
        self.send_response(200, 'OK')
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(bytedata))
        self.end_headers()
        self.wfile.write(bytedata)

    def redirect(self, to):
        self.protocol_version = 'HTTP/2'
        self.send_response(301)
        self.send_header('Location', to)
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.output(read_file("README.md").encode('utf-8'), "text/plain; charset=UTF-8")
        else:
            self.redirect("/index.html")

    def do_POST(self):
        pass

def main():
    with ThreadingHTTPServer((HOST,PORT), LatexRequest) as httpd:
        print(f"Serving latex server on {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
