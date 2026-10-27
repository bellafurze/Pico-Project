import machine
import sys
import utime
import ntptime
LED = machine.Pin("LED", machine.Pin.OUT)
rtc = machine.RTC()
ntptime.settime()
def get_light():
        LED.toggle()
def get_temp():
    temp_sensor = machine.ADC(4)

    conv = 3.3 / (65535)

    temp_read = temp_sensor.read_u16() * conv
    temperature = 27 - (temp_read - 0.706) / 0.001721
    temp = round(temperature, 1)
    return temp

def get_datetime():
        year, month, day, hour, minute, second, dow, doy = rtc.datetime()
        return ("Current date and time {:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(year, month, day, hour, minute, second))
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
    while True:
        get_light()
        print(get_temp())
        utime.sleep(2)

main()