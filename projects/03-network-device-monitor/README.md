# Network Device Monitor (CLI Tool)

## Description:

The Network Device Monitor is a CLI tool that periodically checks the status of a specified list of target devices on the network.

## Features:

- Collects a list of target IP addresses
- Pings each device
- Checks for successful packet delivery
- Display device status
- Periodically repeats the process

## How to Run:

`python main.py`

## Example:

### Input:

```bash
Enter the IP of Devices to Monitor, type 'done' to finish:
:127.0.0.1
:done
```

### Output

```bash
20:17:18
127.0.0.1 is ONLINE
20:17:31
127.0.0.1 is ONLINE
```

## What I Learned:

- Learned to use the subprocess library and how python is able to execute external commands
- Learned how to automate recurring network checks

## Future Improvements:

- Status updates that only display with change in device availability
- add GUI or web version
- Log results to a file for better documentation

## Limitations

- The program uses a simple ping command and might incorrectly categorize devices with ICMP security rules
