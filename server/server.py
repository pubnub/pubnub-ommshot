from Pubnub import Pubnub

import tornado.ioloop
import tornado.web

import base64
import uuid
import time
import re
import s3

## S3 Credentials 
s3_access  = 'AKIAISISGEHX4CHY3KFA'
s3_secret  = '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'
bucket     = 'pubnub-ommshot'
access_url = 'http://%s.s3.amazonaws.com/%s'

## PubNub Credentials
pub_key   = 'pub-c-b8e1ab41-546d-4108-87c8-82d3d8874d3b'
sub_key   = 'sub-c-3b55a087-9faf-11e1-a732-8913f2c5fd35'
sec_key   = 'sec-c-ZDBjNjg4NjktYzNlMi00NWRmLTg2ZDgtZGIxMGFjY2U5ZWY3'
channel   = 'jKSMN7326MQvl4mKIya025XswMU3C3dB7D9kN3FD9de'
origin    = 'ommshot.pubnub.com'

## In-memory Storage of Photo URLs
image_history = []

## Remove all Non-Alphanumeric Characters
rx_alphanumeric = re.compile('[\W_]+')

## PubNub Object
pubnub = Pubnub( pub_key, sub_key, sec_key, False, origin )

## --------------------------------------------------------------------------
## S3 Upload Complete Callback
## --------------------------------------------------------------------------
def upload_complete( response, key ):
    signal( 'complete', data={
        'key' : key,
        'url' : get_s3_url( bucket, key )
    } )

## --------------------------------------------------------------------------
## S3 Upload Wrapper Function
## --------------------------------------------------------------------------
def upload( key, data ):
    signal( 'uploading', data={ 'key' : key } )

    s3.upload(
        s3_access,
        s3_secret,
        bucket,
        key,
        data=data,
        headers={
            'x-amz-acl'      : 'public-read',
            'Content-Type'   : 'image/jpeg',
            'Content-Length' : len(data)
        },
        callback=(lambda response: upload_complete( response, key ))
    )

## --------------------------------------------------------------------------
## Return the URL to the S3 Object
## --------------------------------------------------------------------------
def get_s3_url( bucket, key ):
    return access_url % ( bucket, key )

## --------------------------------------------------------------------------
## Create a Random String
## --------------------------------------------------------------------------
def randomize():
    return rx_alphanumeric.sub( '', base64.encodestring(
        str(uuid.uuid4()) + str(time.time())
    ) )

## --------------------------------------------------------------------------
## Use PubNub to Signal Event State
## --------------------------------------------------------------------------
def signal( event, data='' ):
    return pubnub.publish({
        'channel' : channel,
        'message' : { 'event' : event, 'data' : data }
    })

## --------------------------------------------------------------------------
## Python Tornado Entry Point for Uploading Images
## --------------------------------------------------------------------------
class Upload(tornado.web.RequestHandler):
    def post(self):
        key   = 'images/' + randomize() + '.jpg'
        image = self.request.body or 'Fail'
        upload( key, image )
        self.write('1')

application = tornado.web.Application([
    (r"/upload", Upload)
])

## --------------------------------------------------------------------------
## Running Script from Command Line
## --------------------------------------------------------------------------
def main():
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__": main()
