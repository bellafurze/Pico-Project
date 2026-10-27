import machine
import sys
import utime
def get_light():
        LED = machine.Pin("LED", machine.Pin.OUT)

        while True:
            LED.toggle()
            utime.sleep(2)
def get_temp():
    pass
def get_datetime():
    pass
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
    connect_wifi()
    check_internet()
    while True:
        code = read_morse()
    
        if code == "...---...":
        send_sos()