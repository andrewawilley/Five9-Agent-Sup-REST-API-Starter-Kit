# Usage: python no_cache_server.py [port]

from http.server import HTTPServer, SimpleHTTPRequestHandler

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set headers to prevent caching
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    # Useful for serving files in the current directory
    import sys
    port = 8000 if len(sys.argv) == 1 else int(sys.argv[1])
    server_address = ('', port)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print(f"Serving HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/)...")
    httpd.serve_forever()
