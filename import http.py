import http.server
import socketserver

PORT = 8080
DIRECTORY = r"IAN PORTFOLIO"

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()