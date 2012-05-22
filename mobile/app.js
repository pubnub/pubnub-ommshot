// Upload URL: This will Upload the Photo.
// Change this to point at your Python Server.
var url = "http://192.168.206.164:8888/upload";

// create tab group
var tabGroup = Titanium.UI.createTabGroup();

//
// create base UI tab and root window
//
var win1 = Titanium.UI.createWindow({  
    title:'Photo Beam',
    backgroundColor:'#fff'
});
var tab1 = Titanium.UI.createTab({  
    icon:'KS_nav_views.png',
    title:'Photo Beam',
    window:win1
});
Titanium.UI.setBackgroundColor('#000');

//
// create controls tab and root window
//
var win2 = Titanium.UI.createWindow({  
    title:'Last Beam',
    backgroundColor:'#fff'
});
var tab2 = Titanium.UI.createTab({  
    icon:'KS_nav_ui.png',
    title:'Last Beam',
    window:win2
});

//
//  add tabs
//
tabGroup.addTab(tab1);  
tabGroup.addTab(tab2);  

// open tab group
tabGroup.open();

// Image View
var imageview = Ti.UI.createImageView({
    width: 300,
    height: 400
});
win2.add(imageview);

function takePhoto() { Ti.Media.showCamera({
    success:function(event) {
        Ti.API.debug('Our type was: '+event.mediaType);
        var imgName = 'YourimageName.jpeg'; // or you can set .jpg
        var imgData = event.media;

        imageview.image = imgData;

        var blb    = imageview.toImage();
        var client = Ti.Network.createHTTPClient({
             onload : function(e) {
                 Ti.API.info("Received text: " + this.responseText);
             },
             onerror : function(e) {
                 Ti.API.debug(e.error);
             },
             timeout : 5000  /* in milliseconds */
         });
         client.open("POST", url);
         client.send(blb);
    }
}); }

var button = Titanium.UI.createButton({
   title: 'Beam Photo',
   width: 200,
   height: 80
});
button.addEventListener('click',function(e) {
   Titanium.API.info("You clicked the button");
   takePhoto();
});

win1.add(button);
