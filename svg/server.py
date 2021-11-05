from .canvas import Canvas
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser


def svg_server(canvas: Canvas, port: int = 8000):
    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Python SVG</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(canvas.svg_content(), "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    webServer = HTTPServer(("localhost", port), MyServer)
    print(f"Server started http://localhost:{port}")

    webbrowser.open_new_tab(f"http://localhost:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

