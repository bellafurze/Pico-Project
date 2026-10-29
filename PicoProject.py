# import libraries

# Time library is used to add delays in the code, which can be useful for timing events or creating pauses between actions.
# Sleep function is used to pause the execution of the program for a specified number of seconds.
from time import sleep

# Machine library is used to access the hardware features of the microcontroller
# such as GPIO pins, ADC (Analog-to-Digital Converter)
import machine

# Sys library is used to access system-specific parameters and functions
# such as command-line arguments, standard input/output, and system exit.
import sys

# Utime library is used to access time-related functions, such as getting the current time or measuring elapsed time.
import utime

# Network library is used to access the network features of the microcontroller
# such as connecting to Wi-Fi networks, sending and receiving data over the internet.
import network

# NTP time library is used to synchronize the device's clock with an NTP (Network Time Protocol) server
import ntptime

# Urequests library is used to send HTTP requests and receive responses from web servers.
# HTTP requests are used to communicate with web services and APIs, allowing the device to send and receive data over the internet.
import urequests as requests


# define variable as the LED pin
LED = machine.Pin("LED", machine.Pin.OUT)


# define variable as the WLAN interface for connecting to Wi-Fi networks
# WLAN stands for Wireless Local Area Network, which is a type of network that allows devices to connect to the internet wirelessly.
wlan = network.WLAN(network.STA_IF)

# define the SSID and password for the Wi-Fi network to connect to
# In the Thonny file,  we created a seperate file called secrets.py to store the SSID and password for the Wi-Fi network.
# in our personal files we called secrets.py as a library and imported the SSID and password from it for security reasons.
ssid = 'NAME OF YOUR WIFI NETWORK'
password = 'YOUR SECRET PASSWORD'

# define functions
def connect_wifi():
    # activate wlan on the pico and input the SSID and password to connect to the Wi-Fi network
    wlan.active(True)
    wlan.connect(ssid, password)

    # continue trying to connect to the Wi-Fi network until a connection is established
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print('Connected')

def get_temp():

    # naming the part of the board that has the temperature sensor
    temp_sensor = machine.ADC(4)

    # highest voltage of the pico 3.3V and the highest value amount of voltage any analog can send thus the conversion factor is 3.3/65535
    conv = 3.3 / (65535)

    # read the temperature sensor and convert the value to Celsius
    temp_read = temp_sensor.read_u16() * conv
    temperature = 27 - (temp_read - 0.706) / 0.001721
    temp = round(temperature, 1)
    return temp

def get_datetime():

    # Get the current date and time from the RTC
    # RTC means Real Time Clock, which is a hardware component 
    # It keeps track of the current time and date even when the device is powered off.
    year, month, day, _, hour, minute, second, _ = machine.RTC().datetime()

    # Return the date and time in a formatted string as "YYYY-MM-DD HH:MM:SS"
    return "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(year, month, day, hour, minute, second)


def get_light():

    # When Pico is connected to the computer, the LED is on.
    LED.toggle()


def get_ip():

    # get the IP address of the connection to the Wi-Fi network using the ipify website
    r = requests.get('http://api.ipify.org')
    
    # strip the given ip address of any whitespace characters and return it as a string and return the IP address
    ip = r.text.strip()
    r.close()
    return ip

def get_mac():

    # Get the MAC address of the device's network interface. 
    # MAC stands for Media Access Control
    # This is a unique identifier assigned to network interfaces for communication on a network.
    mac = wlan.config('mac')

    # Format the MAC address as a string of hexadecimal values (a base-16 number system) separated by colons.
    return ':'.join('{:02x}'.format(b) for b in mac)

def check_internet():
    pass

def read_morse():
    pass

def send_sos():
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