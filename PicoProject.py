# import libraries
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
def get_light():
        
        # while everything is true, toggle the LED and sleep for 2 seconds
        while True:
            LED.toggle()
            utime.sleep(2)
def get_temp():
    pass
def get_datetime():
    machine.RTC().datetime((year, month, day, 0, hour, minute, second, 0))

    print("Date and Time: {:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(year, month, day, hour, minute, second))
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        utime.sleep(1)
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
    pass
