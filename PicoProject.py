# import libraries
from time import sleep

import machine
import sys
import utime
import network
# define variable as the LED pin
LED = machine.Pin("LED", machine.Pin.OUT)
# ntptime.settime()

ssid = 'NAME OF YOUR WIFI NETWORK'
password = 'YOUR SECRET PASSWORD'

# define functions
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        print(wlan.ifconfig())

def get_temp():
    temp_sensor = machine.ADC(4)

    conv = 3.3 / (65535)

    temp_read = temp_sensor.read_u16() * conv
    temperature = 27 - (temp_read - 0.706) / 0.001721
    temp = round(temperature, 1)
    return temp

def get_datetime():
    machine.RTC().datetime((year, month, day, 0, hour, minute, second, 0))

    print("Date and Time: {:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(year, month, day, hour, minute, second))


def get_light():       
    # while everything is true, toggle the LED and sleep for 2 seconds
    LED.toggle()




def get_ip():
    pass

def get_mac():
    pass

def check_internet():
    pass

def send_sos():
    pass

def read_morse():
    pass

def main():
    connect_wifi()
    get_light()
    get_temp()
    get_datetime()
    get_ip()
    get_mac()
    check_internet()
    send_sos()
    read_morse()


main()