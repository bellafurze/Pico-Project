# import libraries
from time import sleep

import machine
import sys
import utime
import network
import ntptime
import urequests as requests
# define variable as the LED pin
LED = machine.Pin("LED", machine.Pin.OUT)
wlan = network.WLAN(network.STA_IF)

ssid = 'NAME OF YOUR WIFI NETWORK'
password = 'YOUR SECRET PASSWORD'

# define functions
def connect_wifi():
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print('Connected')

def get_temp():
    temp_sensor = machine.ADC(4)

    conv = 3.3 / (65535)

    temp_read = temp_sensor.read_u16() * conv
    temperature = 27 - (temp_read - 0.706) / 0.001721
    temp = round(temperature, 1)
    return temp

def get_datetime():
    year, month, day, _, hour, minute, second, _ = machine.RTC().datetime()
    return "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(year, month, day, hour, minute, second)


def get_light():       
    # while everything is true, toggle the LED and sleep for 2 seconds
    LED.toggle()




def get_ip():
    r = requests.get('http://api.ipify.org')
    ip = r.text.strip()
    r.close()
    return ip

def get_mac():
    mac = wlan.config('mac')
    return ':'.join('{:02x}'.format(b) for b in mac)

def check_internet():
    pass

def send_sos():
    pass

def read_morse():
    pass

def create_JSON():
    pass

def main():
    connect_wifi()
    ntptime.settime()
    get_light()
    print(get_temp())
    print(get_datetime())
    print(get_ip())
    print(get_mac())
    check_internet()
    read_morse()
    send_sos()


main()