#!/usr/bin/env python3

from envirophat import light
from envirophat import weather
from envirophat import motion
import time
import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client
import random # this be here for testing

print("test the code")

# set up OSC stuff
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()
  client = udp_client.SimpleUDPClient(args.ip, args.port)


# send values from enviro pHAT
def readAndSendValues():
    while True:
        # print(light.light())
        # print(light.rgb())
        # print(weather.temperature())
        # print(weather.pressure())
        x, y, z = motion.accelerometer()
        print(x, y, z)
        client.send_message("/x", x)
        client.send_message("/y", y)
        client.send_message("/z", z)
        time.sleep(0.01)


readAndSendValues()
