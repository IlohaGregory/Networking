# Packet Sniffer (CLI Tool)

## Description:

The Packet Sniffer is a CLI tool that uses raw sockets to capture and inspect IPv4 packet headers on the local host.

## Features:

- Creates a raw socket and binds it to local host
- Enables OS promiscuous mode to expose packets
- Prints out header information of captured packet

## How to Run:

Ensure IDE runs as administrator
`python main.py`

## Example:

### Input:

N/A

### Output

```bash
Source Address:
127.0.0.1
Destination Address:
127.0.0.1
Protocol: TCP
```

## What I Learned:

- Learned about python raw sockets and how packets can be observed through them
- Learned how packets are created, encapsulated and their flow path within a host
- Deepened my understanding of the IPv4 Header, how protocol fields are packed into bytes
- Learned how raw packet data can be interpreted using protocol specifications

## Future Improvements:

- Continuous packet capture
- Protocol filtering
- Display additional IPv4 header fields
- Log captured packets to a file

## Problems Encountered

- Had a really hard time building a mental model of the OS exposes packets to raw sockets
- Figuring out what feilds were represented by the extracted bytes

## Limitations

- Requires the enabling of promiscious mode which could be a security risk
- No control over what packets are captured
