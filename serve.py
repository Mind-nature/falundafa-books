import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(os.environ.get("PORT", 8080))
handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port} from {os.getcwd()}")
    httpd.serve_forever()
