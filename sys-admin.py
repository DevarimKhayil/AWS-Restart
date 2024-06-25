import os
import subprocess
os.system("ls")
print("\n")
subprocess.run(["ls"])
print("\n")
subprocess.run(["ls", "-l"])
print("\n")
subprocess.run(["ls","-l","README.md"])
print("\n")
command="uname"
commandArgument="-a"
print(f"Gathering sysytem information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


