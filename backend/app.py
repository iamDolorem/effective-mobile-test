from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit

MESSAGE = b"Hello from Effective Mobile!\n"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(MESSAGE)))
            self.end_headers()
            self.wfile.write(MESSAGE)
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found\n")

    def log_message(self, format, *args):
        return

def main():
    host = "0.0.0.0"
    port = 8080
    httpd = HTTPServer((host, port), Handler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
