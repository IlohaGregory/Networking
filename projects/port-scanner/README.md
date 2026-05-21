# Port Scanner (CLI Tool)

## Description:

The Port Scanner is a simple Python tool that is used to check what ports are open on a target device.

## Features:

- Parse IP address and port scan range
- Attempt TCP connection across a specified ports range
- Shows what ports are opened in the range
- Implemented test server for local host connections

## How to Run:

`python main.py`
(To target local host also run test_server.py in a seperate terminal)

## Example:

### Input:

```bash
python main.py
Target IP: 127.0.0.1
Start Port: 9998
End Port: 10001
```

### Output:

```bash
Port 9999 is open
```

## What I Learned:

- Learned how python makes socket connections with the help of the OS networking API
- Learned how to establish server client connections and how to send messages between them
- Learned the importance of resource handling

## Future Improvements:

- rohbust input validation
- timeout handling
- port validation
- service/banner detection

## What is broken:

- if target device does not reject/accept the tool could wait endlessly for a response
