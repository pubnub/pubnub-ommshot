# PubNub OmmShot - Real-time Mobile Photo Sync

OmmShot is a stack of technologies that allow mobile cameras to broadcast
photo binary data in real-time to millions of viewers synchronously.
This is a simple stack which uses a Mobile Phone and PubNub to sync
live real-time photo data between many end points.
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
 2. WebView  ./webview - Consumer: Viewing Real-time Photos.
 3. Server   ./server  - Middle component which coordinates
    *Uploads* and *Downloads* 
    Utilizing PubNub Cloud as the Signaling Mechanism.
 4. Test     ./test    - Upload Simulation Test

## Receiving Photo Stream

