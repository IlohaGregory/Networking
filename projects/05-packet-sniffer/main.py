import socket

HOST = "127.0.0.1" # loopback address for host addressing

# Create raw socket
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
raw_socket.bind((HOST, 0))

# set socket options to include IP header
raw_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# enable promiscuios mode for packet exposure
raw_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# observe exposed packet
packet, addr = raw_socket.recvfrom(65565)
# match protocol
if packet[9] == 17:
    protocol = "UDP"
elif packet[9] == 6:
    protocol = "TCP"
else:
    protocol = "ICMP"
source_addr = packet[12:16]
dest_addr = packet[16:20]
# print source and destination address
print("Source Address: ")
print(*source_addr, sep=".")
print("Destination Address: ")
print(*dest_addr, sep=".")
print(f"Protocol: {protocol}")


