# Sensors from the EnviropHAT sonified in PureData

* Needs Raspberry Pi W with Jessie or Stretch
* Do the OTG thing: https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a
* Make sure the Pi Zero is POWERED WELL. For the amp it needs separate power otherwise will keep rebooting!!
* Stick the EnviroPHAT and Adafruit Speaker Bonnet on.
* Install both the softwares:
* EnviroPHAT: https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
* https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi/overview
* when installing, choose NO when it prompts to do the thing to reduce popping!!
* install pd: apt-get install pd
* install pip3 install python-osc
* run it with python3
* This should work.

### STARTPD.service:

[Unit]
Description=Start Pd

[Service]
User=pi
WorkingDirectory=/home/pi/envirosound
ExecStart=/usr/bin/pd -nogui /home/pi/envirosound/envirosound.pd
Restart=on-failure

[Install]
WantedBy=multi-user.target

### STARTPYTHON.service:

[Unit]
Description=Start Python
Wants=STARTPD.service

[Service]
User=pi
WorkingDirectory=/home/pi/envirosound
ExecStart=/usr/bin/python3 /home/pi/envirosound/getenvirosensors.py
Restart=on-failure

[Install]
WantedBy=multi-user.target

### Make sure both startup scripts are executable

sudo chmod +x STARTPD.service
sudo chmod +x STARTPYTHON.service

### make sure both scripts are enabled

sudo systemctl enable STARTPD.service
sudo systemctl enable STARTPYTHON.service

### start to test 'em
sudo systemctl start STARTPD.service
sudo systemctl start STARTPYTHON.service

### check logs if it doesnt work

cat /var/log/syslog

### to stop and tweak them
sudo systemctl stop STARTPD.service
sudo systemctl stop STARTPYTHON.service
