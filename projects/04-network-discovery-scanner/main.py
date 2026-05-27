import ipaddress
import subprocess
import time

entry = input("Enter IP address and CIDR:\n")

while True:
    try:
        submask = ipaddress.IPv4Network(entry, strict= True)
        ip = ipaddress.IPv4Interface(entry)
        break
    except ValueError:
        print("Enter a valid IP address")

# create a list of all hosts possible host in the range
hosts = list(submask.hosts())
online_hosts = []
start_time = time.perf_counter() # time process
# check the status of each host
print("\nOnline Hosts: ")
for host in hosts:
    status = subprocess.run(['ping', '-n', '1', '-w', '1000', str(host)], capture_output= True, text= True) # ping hosts to determine status
    # if no error hos is online
    if status.returncode == 0:
        print(f"{host} is ONLINE")
        online_hosts.append(str(host))
end_time = time.perf_counter()

print(f"\nTotal Number of Online Hosts: {len(online_hosts)}")
print(f"Time Elapsed: {(end_time - start_time):.2f} seconds")
print(f"Percentage Online: {((len(online_hosts)/len(hosts)) * 100):.2f}%")