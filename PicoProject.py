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

# Ujson library is used to encode and decode JSON (JavaScript Object Notation) data, 
# This is a lightweight data format used for exchanging data between devices and web services.
import ujson as json


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

# define variable as the input pin for the wires connected to the Pico
pin_in = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

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
    try:
        r = requests.get('http://example.com')
        print('Status code:', r.status_code)
        OK = r.status_code == 200
        r.close()
        return OK
    except OSError:
        print('No internet connection')
        return False

# define a function to check if the wires are connected to the Pico    
def wires_connected():

    # Check if the input pin is low (0) or high (1) to determine if the wires are connected to the Pico
    if pin_in.value() == 0:
        return True
    else:
        return False

# define a function to read Morse code signals from the wires connected to the Pico
def read_morse():

    # Initialize an empty string to store the Morse code signals received from the wires connected to the Pico
    signals = ""

    # Start an infinite loop to continuously check for Morse code signals from the wires connected to the Pico
    while True:

        # Record the current time in milliseconds to use as a reference point for timing the Morse code signals
        # utime.ticks_ms() returns the number of milliseconds since the device was last reset
        WaitStart = utime.ticks_ms()

        # Check if the wires are connected to the Pico. If not, wait for a signal to be received.
        while not wires_connected():

            # If the wires are not connected to the Pico and more than 2 seconds have passed since the last signal was received
            # print the received signals and check if they match the Morse code for SOS ("...---...").
            if signals and utime.ticks_diff(utime.ticks_ms(), WaitStart) > 2000:
                print("Received:", signals)
                return signals == "...---..."

            # If the wires are not connected to the Pico, wait for 10 milliseconds before checking again.
            utime.sleep_ms(10)

        # If the wires are connected to the Pico
        # turn on the LED to indicate that a signal is being received and record the current time in milliseconds.
        LED.on()
        StartTime = utime.ticks_ms()

        # Wait for the wires to be disconnected from the Pico, indicating that the signal has ended.
        while wires_connected():
            utime.sleep_ms(10)

        # Turn off the LED to indicate that the signal has ended and calculate the time elapsed since the signal started.
        LED.off()
        TimePassed = utime.ticks_diff(utime.ticks_ms(), StartTime)

        # Based on the time elapsed, determine if the signal received is a dot (short signal) or a dash (long signal)
        # add it to the signals string.
        if TimePassed < 50:
            continue
        elif TimePassed <= 500:
            print("dot")
            signals += "."
        else:
            print("dash")
            signals += "-"

# define a function to send an SOS message to a specified URL with the given data
def send_sos(url, data):

    # Send an HTTP POST request to the specified URL with the given data as JSON
    try:

        # Set the Content-Type header to application/json to indicate that the data being sent is in JSON format
        # requests.post() sends an HTTP POST request to the specified URL with the given data and headers
        # The response from the server is stored in the variable r and json.dumps() converts the data dictionary to a JSON-formatted string
        r = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

        # Print the status code of the response received from the server to indicate whether the request was successful or not
        print('Status code:', r.status_code)
        OK = r.status_code == 200
        r.close()

    # Handle any OSError exceptions that may occur during the HTTP request and print an error message if the request fails
    except OSError:
        print('Could not send SOS message')
        return False
    if OK:
        print("Help is on it's way")
    else:
        print("Something went wrong, try again")
    return OK
    
# define a function to create a JSON file with the current date and time, temperature, IP address, and MAC address of the device
def create_JSON():

    # Create a dictionary with the current date and time, temperature, IP address, and MAC address of the device
    dict = {
        #replace NAME with your name
        "name": "NAME", 
        "msg": "SOS",
        "dt": get_datetime(),
        "celsius": get_temp(),
        "ip": get_ip(),
        "mac": get_mac()
    }

    # Write the dictionary to a JSON file named "data.json" using the json.dump() function
    with open("data.json", "w") as f:
        json.dump(dict, f)
    return dict

# define the main function to connect to Wi-Fi, synchronize time, get sensor data, and send an SOS message 
# if the correct Morse code is received
def main():

    # Connect to Wi-Fi and synchronize the device's clock with an NTP server
    connect_wifi()

    # Synchronize the device's clock with an NTP server to ensure accurate timekeeping
    ntptime.settime()

    # Get light gets the light level from the LED and prints it to the console
    get_light()

    # prints the current temperature, date and time, IP address, MAC address, and whether the wires are connected to the Pico
    print(get_temp())
    print(get_datetime())
    print(get_ip())
    print(get_mac())
    print(wires_connected())
    check_internet()

    # If the correct Morse code for SOS is received, create a JSON file with the current date and time, temperature, IP address, and MAC address of the device,
    # send an SOS message to a specified URL with the JSON data. If the Morse code is incorrect, print an error message.
    if read_morse():
        print("SOS Morse code recognized!")

        # data is a dictionary that contains the current date and time, temperature, IP address, and MAC address of the device
        data = create_JSON()

        # send the SOS message to this url with the JSON data
        url = "https://cpnits.com/sosapi/help"
        send_sos(url, data)

    # If the Morse code received is incorrect, print an error message indicating that the Morse code is incorrect.
    else:
        print("Incorrect Morse code received.")

# Call the main function to start the program
main()