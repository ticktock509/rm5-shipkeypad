import time
import ubinascii
import machine, uos
import network
#import urequests as requests
import os
print('end on import')
import rp2
from secrets import secrets
from simple import MQTTClient
rp2.country('US')
ssid = secrets['ssid']
pw = secrets['pw']

nic = network.WLAN(network.STA_IF)

nic.active(True)
nic.config(pm = 0xa11140)
nic.connect(ssid, pw)

led = machine.Pin('LED', machine.Pin.OUT)
for x in range(3):
    led.on();
    time.sleep(.1)
    led.off();
    time.sleep(.1)
    

if not nic.isconnected():
    print("Waiting for connection...")
    while not nic.isconnected():
        led.on();
        time.sleep(.1)
        led.off();
        time.sleep(.1)

print('Connection successful')
led.on();
print('end of boot')