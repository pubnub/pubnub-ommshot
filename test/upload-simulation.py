import tornado.ioloop
import tornado.httpclient

def read(f):
    try:
        fh   = open( f, 'r' )
        data = fh.read()
        fh.close()
    except:
        data = 0

    return data

loop   = tornado.ioloop.IOLoop.instance()
http   = tornado.httpclient.AsyncHTTPClient()
method = 'POST'
url    = 'http://192.168.206.164:8888/upload'
image  = (read('image.jpg') or '_')

def complete(info):
    print(info)
    loop.stop()

http.fetch(
    url,
    method=method,
    callback=complete,
    body=image
)

## -----------------------------------------------------------------------
## IO Event Loop
## -----------------------------------------------------------------------
loop.start()
