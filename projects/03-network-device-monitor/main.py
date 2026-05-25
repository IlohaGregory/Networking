import subprocess
import time
import ipaddress
from datetime import datetime

# function to check and print status
def check_status(addr_list):
    for addr in addr_list:
        ping = subprocess.run(['ping', addr], capture_output= True, text= True)
        # check if at least 1 packet was delivered and print status
        if ping.returncode == 0:
            print(f"{addr} is ONLINE")
        else:
            print(f"{addr} is OFFLINE")

# List to store IP addresses
addr_list = []
print("Enter the IP of Devices to Monitor, type 'done' to finish:")
while True:

    try:
        # collect user input
        addr = input(":")
        # check current input
        if addr.lower() == 'done':
            if not addr_list:
                raise SystemExit("No Addresses Given!!!") # kill program if no address is provided
            break # proceed if user types done
        ipaddress.IPv4Interface(addr) # simple address check
        addr_list.append(addr) # add address to address list
    except ipaddress.AddressValueError:
        print("Enter a Valid IP address")
while True:
    print(datetime.now().strftime("%H:%M:%S"))
    check_status(addr_list)
    time.sleep(10)