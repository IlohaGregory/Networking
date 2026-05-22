import socket

target_ip = input("Target IP: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

active_ports = []
# scan ports from start to end, ignore OSERRORS for invalid ports
for port in range(start_port, end_port + 1):
    try:
        # initialize server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        client.connect((target_ip, port))
        active_ports.append(port)
        client.close()
    except OSError:
        pass

if not active_ports:
    print("No active ports in the range")

# print out all active ports
for port in active_ports:
    print(f"Port {str(port)} is open")

