# import libraries
import machine
import sys
import utime

# define functions
def get_light():
        # define variable as the LED pin
        LED = machine.Pin("LED", machine.Pin.OUT)

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
    pass
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
