# PubNub OmmShot - Real-time Mobile Photo Sync

OmmShot is a stack of technologies that allow mobile cameras to broadcast
photo binary data in real-time to millions of viewers synchronously.
This is a simple stack which uses a Mobile Phone and PubNub to sync
live real-time photo data between many end points. 
Example use cases are

- Live Blog Photo Stream via Mobile Phone
- Instant Backup of Photos While to Online
- Remote and Non-stationary Security Monitoring Systems

This repository contains the three pieces necessary to synchronize photo
data in real-time starting at the Mobile Camera Phone as the source
producer of the Image Content.
The intermediate component is a python server which captures the photo data
transmission and deploys to the storage service.
In this case we are using S3.
The final component is a viewer or 

Note that a mandatory cloud service is being utilized for the coordination
of all real-time events.
PubNub provides the pivotal component that provides real-time human presence
for mobile and web apps.
By pressing the "Shoot Camera" button on your phone, PubNub will signal
viewers on the other end that a new photo is available.

## Directory Explanation

 1. Mobile   ./mobile  - Producer: Holds the Photo App to run on
    the iPhone/Android Phone.
    Based in Titanuim Mobile SDK: http://www.appcelerator.com/
 2. WebView  ./webview - Consumer: Viewing Real-time Photos.
    Load this page to see the photos streamed to your browser
    instantly as the are Snapped with a Mobile Camera.
 3. Server   ./server  - Middle component which coordinates
    *Uploads* and *Downloads*.
    Utilizing PubNub Cloud as the Signaling Mechanism.
 4. Test     ./test    - Upload Simulation Test

## API Keys

Note that this Repository includes WORKING API Keys.
It is a good idea to obtain your own API keys.

 1. Open `./server/server.py` and replace PUBNUB and S3 Credentials.
    PubNub Credentials available via http://www.pubnub.com
    and S3 Credentials available via http://aws.amazon.com/s3/
 2. Open `./webview/viewer.html` and replace PUBNUB Credentials.

## Setup of Code

You will need to install the mobile app on your phone, then
run the Python Web Server, finally open the `viewer.html` file
to see the photos stream in as you capture them via your mobile phone.

#### Web Server Handeler Setup: Python

Install Python Tornado via
`sudo pip install tornado`
or download source http://www.tornadoweb.org/

Then execute python ./server/server.py

#### Mobile Titanium Setup

Build Mobile Component with Titanium by dropping in the `app.js`
file found in the `mobile` directory.

Replace `url` var for upload photo.
This is found inside the `./mobile/app.js` JavaScript File.

Install app on your mobile phone and launch.

#### Website View

Open `./webview/viewer.html` in a web browser.

