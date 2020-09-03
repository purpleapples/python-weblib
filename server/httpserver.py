from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
port: int = 8888


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        result_path = urlparse(self.path)

        # send response status
        self.send_response(200)

        # send header info
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        print(result_path)
        print(f'{result_path.path}, {result_path.path == "/usr" }')
        if result_path.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.wfile.write('<h1>메인페이지 입니다.</h1>'.encode('utf-8'))

        elif result_path.path == '/usr':
            print('usr usr')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.wfile.write('<h1>사용자메뉴 입니다.</h1>'.encode('utf-8'))

        elif result_path.path == '/board':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.wfile.write('<h1>게시판입니다.</h1>'.encode('utf-8'))


httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f'Server Running on Port {port}')
httpd.serve_forever()

