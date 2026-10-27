def led_on():
def led_off(): 
def get_temp():
def get_datetime():
def connect_wifi():
def get_ip():
def get_mac():
def check_internet():
def send_sos():
def read_morse():
def main():
    connect_wifi()
    check_internet()
    while True:
        code = read_morse()
        
        if code == "...---...":
        send_sos()