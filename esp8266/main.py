import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Xiaomi_3BC7', '9496!0409')
sta_if.isconnected()
print(sta_if.ifconfig())

import simple
import time
import json

from machine import Pin
p2 = Pin(2, Pin.OUT)

def ctrl_cb(topic, msg):
  data_dict = json.loads(msg)
  if data_dict['idx'] == 1:
    print("it's me")
    print('state: ' + str(data_dict['nvalue']))
    p2.value(data_dict['nvalue'])
    
  print(data_dict)

c = simple.MQTTClient('esp8266', '192.168.31.177', 1883)
c.set_callback(ctrl_cb)
c.connect()
c.subscribe('domoticz/out')

while True:
  c.check_msg()
  time.sleep_ms(200)
