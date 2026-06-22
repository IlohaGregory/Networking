import paramiko # type: ignore

# Initialize client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# get input and authenticate
while True:
    try:
        addr = input("Enter IP Address: ")
        user_name = input("Username: ")
        password = input("Password: ")
        print("Connecting to host....")
        client.connect(hostname= addr, username=user_name, password=password)
        print("connected")
        break
    except paramiko.ssh_exception.AuthenticationException:
        print("Error: Invalid password")
    except TimeoutError:
        print("Error: Timeout, try again")

cmd = input("Enter Command:  ")
stdin, stdout, stderr = client.exec_command(cmd)
error = stderr.read().decode("utf-8")
if error:
    print(f"Error: {error}")
else:
    print(stdout.read().decode("utf-8"))

# close connection
client.close()