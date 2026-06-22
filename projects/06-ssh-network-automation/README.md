# SSH Network Automation (CLI Tool)

## Description:

The SSH Network Automation is a CLI tool that uses the paramiko library to establish a connection to a remote host, execute commands and output the result on the client terminal.

## Features:

- Collects ssh credentials and establishes a connection
- Parses commands and provides output
- Error handling

## How to Run:

`python main.py`

## Example:

### Input:

```bash
Enter IP Address: localhost
Username: BLESSED
Password: blessed
Connecting to host....
connected
Enter Command:  whoami
```

### Output

```bash
desktop-adkrvo8\blessed
```

## What I Learned:

- Learned to use the Paramiko library to automate ssh connections
- Deeper understanding of stdout, stderr, stdin and how python handles them

## Future Improvements:

- SSH into multiple hosts
- Saving output into a file
- Reading ssh credentials from a file
- Terminal mode for CISCO IOS devices

## Problems Encountered

- Setting up local ssh server for testing

## Limitations

- The tool can only connect to one host at a time
- Requires an SSH server to be configured and running on the target host
- Credentials are entered in plain text and are not securely stored
- No interactive shell
