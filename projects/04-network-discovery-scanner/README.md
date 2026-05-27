# Network Discover Scanner (Windows CLI Tool)

## Description:

The Network Discovery Scanner is a CLI tool that scans the address range of the provided IP's network and outputs a list of devices that are currently online.

## Features:

- Collects an IP address in CIDR notation
- Pings each device in the provided IP network range
- Checks for successful packet delivery
- Display device status, Number of Online hosts and time elapsed

## How to Run:

`python main.py`

## Example:

### Input:

```bash
Enter IP address and CIDR:
127.0.0.0/29
```

### Output

```bash
Online Hosts:
127.0.0.1 is ONLINE
127.0.0.2 is ONLINE
127.0.0.3 is ONLINE
127.0.0.4 is ONLINE
127.0.0.5 is ONLINE
127.0.0.6 is ONLINE

Total Number of Online Hosts: 6
Time Elapsed: 0.44 seconds
Percentage Online: 100.00%
```

## What I Learned:

This project was the cummulation of the work i have done so far

- I developed a deeper understanding of some of the primitives I have been working with
- I learned the importance of considering execution time and the trade-offs required

## Future Improvements:

- Parallel scanning
- Mini network mapper
- add GUI or web version
- Log results to a file for better documentation

## Limitations

- The program uses ping command tailored to window OS
