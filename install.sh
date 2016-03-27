ln simple-fileshare.service /etc/systemd/system/simple-fileshare.service
mkdir -p /tmp/simple-fileshare/files/
chmod 777 /tmp/simple-fileshare/files/

read -p "Type the name of the 'bucket' that you would like to create" FIRST_BUCKET
mkdir /tmp/simple-fileshare/files/"$FIRST_BUCKET"
chmod 777 /tmp/simple-fileshare/files/"$FIRST_BUCKET"
ln -s /tmp/simple-fileshare/files/"$FIRST_BUCKET" www/"$FIRST_BUCKET"

systemctl enable simple-fileshare.service
systemctl daemon-reload
