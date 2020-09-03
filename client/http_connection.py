from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')


# GET / HTTP/1.1
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)

if resp.status == 200:
    body = resp.read()
    print(body)
    print(type(body))



# connection failure

conn.request('GET', '/hello.html')

resp = conn.getresponse()
print(resp.status, resp.reason)