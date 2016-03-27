# simple-fileshare

A very simple filesharing server for uploading and sharing files on a (private) network.

# Screenshots
![alt text](http://i.imgur.com/obTTZLQ.png "Uploading")
![alt text](http://i.imgur.com/ovYMfyY.png "Browsing folders")
![alt text](http://i.imgur.com/1gX7Oeo.png "Downloading files")
![alt text](http://i.imgur.com/4YI3B1B.png "Managing folders")


# Installation
```
# clone the repo into a folder that can be read by all users
git clone https://github.com/robert-blankenship/simple-fileshare/ /home/simple-fileshare

# then, run the installer script
cd /home/simple-fileshare
./install.sh
./simple-fileshare
```

## Requirements
'simple-fileshare' has very few requirements:
  - linux
  - systemd
  - python2.7 or greater
