#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import asyncio

class App(BaseHTTPRequestHandler):

    _routes = {}
    def __init__(self):
        return

    def do_GET(self):
        url_parsed = urllib.parse.urlparse(self.path)
        if url_parsed.path not in self._routes:
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        query = url_parsed.query
        res = self._routes[url_parsed.path](self)
        self.wfile.write(bytes(res, "utf-8"))


    def __call__(self, *args, **kwargs):
        """Handle a request."""
        super().__init__(*args, **kwargs)

    def route(self, *argv, **kwargs):
        path = argv[0]
        def register_fn(fn):
            # register route and function
            self._routes[path] = fn
            return fn # do not call function #(*argv[1:], **kwargs)
        return register_fn

    def get_registered_routes(self):
        return self._routes

    def start_server(self, host='localhost', port=5555):
        # server part
        self._httpd = HTTPServer((host, port), self)
        print("server started.")
        self._httpd.serve_forever()

    def stop_server(self):
        self._httpd.server_close()
        print("server stopped.")


app = App()

@app.route('/test')
def test(app):
    return "xx"

@app.route('/hello')
def hello(app):
    return "hello"

print("registred routes")
print("\n".join(app.get_registered_routes()))



def main():
    try:
        app.start_server()
    except KeyboardInterrupt:
        pass


main()







