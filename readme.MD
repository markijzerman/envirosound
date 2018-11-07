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
* install the python library needed: pip3 install python-osc
* run "pd &", load up the patch "envirosound.pd" and make sure you have sound
* run "python3 getenvirosensors.py" and make sure the values are being passed to Pd.
* This should work.

## To make it run on startup
To make the python script and the PD patch run on start-up, we want to use systemd.
Systemd is a system to start and stop services.
We make two systemd files. One to start pd, and one to start python.
They need to be started in that order!
The Pd one needs to "sleep" for 10 seconds before it runs, to make sure the audio drivers are ready. This is a hack, and I still need to figure out a nicer way of doing this.

The files should be made in /etc/systemd/system and called STARTPD.service and STARTPYTHON.service
Make sure they point to the right files. In my case all the files of this repo are in /home/pi/envirosound.

#### STARTPD.service:

[Unit]  
Description=Start Pd  

[Service]  
ExecStartPre=/bin/sleep 10
User=pi  
WorkingDirectory=/home/pi/envirosound  
ExecStart=/usr/bin/pd -nogui /home/pi/envirosound/envirosound.pd  
Restart=on-failure  

[Install]  
WantedBy=multi-user.target  

#### STARTPYTHON.service:  

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

#### enable scripts to make them start on startup

sudo systemctl enable STARTPD.service  
sudo systemctl enable STARTPYTHON.service  

#### start to test the scripts
sudo systemctl start STARTPD.service  
sudo systemctl start STARTPYTHON.service  

#### check logs if it doesnt work  

systemctl status STARTPD
systemctl status STARTPYTHON

#### to stop and tweak them if needed...
sudo systemctl stop STARTPD.service  
sudo systemctl stop STARTPYTHON.service  
