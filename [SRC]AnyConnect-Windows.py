# Creator: Milan Kopac
# Created: 24.7.2023
# Note:
# Obfuscation (if implemented): python -OO -m py_compile AnyConnect-Windows.py

import os
import inquirer
import subprocess
from bs4 import BeautifulSoup

# Global definitions
ListOfAvailableConnections = []

AnyConnectProfilesPath = 'c:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\Profile'
AnyConnectVpnCli = 'c:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpncli.exe'

#Feed connections from XML
for filename in os.listdir(AnyConnectProfilesPath):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(AnyConnectProfilesPath, filename)
    
    # Open XML file and read data
    with open(fullname, 'r') as f:
        data = f.read()
    # Passing the stored data inside the beautifulsoup parser, storing the returned object
        Bs_data = BeautifulSoup(data, "xml")
    # Using find() to extract attributes of the first instance of the tag
        Hostname = Bs_data.find('HostName').string
    # Show the value
    #    print(b_name)
    # Add the Hostname to the list
        ListOfAvailableConnections.append(Hostname)

# Made an user to select a connection
questions = [
    inquirer.List('ConnectionType',
                message="Select a connection:",
                choices=[connection for connection in ListOfAvailableConnections],
            ),
]
answers = inquirer.prompt(questions)
answer = answers["ConnectionType"]

questions = [
    inquirer.List('ConnectionType',
                message="Select an action:",
                choices=['connect', 'disconnect', 'status'],
            ),
]
answers = inquirer.prompt(questions)
answer = answers["ConnectionType"]

if answer == 'connect':
    # Call vpncli.exe session to connect
    subprocess.run([AnyConnectVpnCli, f'connect', answer, f'-s'])
elif answer == 'disconnect':
    # Call vpncli.exe session to disconnect
    subprocess.run([AnyConnectVpnCli, f'disconnect', answer])
elif answer == 'status':
    # Call vpncli.exe to show status
    subprocess.run([AnyConnectVpnCli, f'status', answer])
else:
    #Exception
    print("The action choice selected doesn't exist. Contact developer.")