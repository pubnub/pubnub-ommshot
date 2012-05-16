import tornado.ioloop
import tornado.web

from Pubnub import Pubnub

channel    = 'jKSMN7326MQvl4mKIya025XswMU3C3dB7D9kN3FD9de'
imagestore = { '1' : 'NoneNoneNoneNoneNone' }
pubnub     = Pubnub( 'demo', 'demo', '', False, 'pubsub.pubnub.com' )

class Upload(tornado.web.RequestHandler):
    global imagestore;
    global pubnub;

    def post(self):
        imagestore['1'] = self.request.body or 'Fail'
        pubnub.publish({
            'channel' : channel,
            'message' : 'URL'
        })
        self.write('1')


class Beam(tornado.web.RequestHandler):
    global imagestore;
    def get(self):
        self.set_header( "Access-Control-Allow-Methods", "GET" )
        self.set_header( "Access-Control-Allow-Origin", "*" )
        self.set_header( "Cache-Control", "no-cache" )
        self.set_header( "Content-Type", "image/jpeg" )
        self.write(imagestore['1'])

application = tornado.web.Application([
    (r"/upload", Upload),
    (r"/beam", Beam),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
