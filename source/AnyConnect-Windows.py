# Creator: Milan Kopac
# Created: 24.7.2023
# Version: 1.0.1
# Note: You need to have profiles in Cisco ProgramData as XML files with HostName!
# Obfuscation (if implemented): python -OO -m py_compile AnyConnect-Windows.py
# Modules installation:
#	pip install inquirer
#	pip install BeuatifulSoup
#	pip install bs4
#	pip install lxml

import os
import inquirer
import subprocess
import sys
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
HostNameQuestions = [
    inquirer.List('ConnectionType',
                message="Select a connection:",
                choices=[connection for connection in ListOfAvailableConnections],
            ),
]
HostNameAnswers = inquirer.prompt(HostNameQuestions)
HostNameAnswer = HostNameAnswers["ConnectionType"]

ActionQuestions = [
    inquirer.List('ActionType',
                message="Select an action:",
                choices=['connect', 'disconnect', 'status'],
            ),
]
ActionAnswers = inquirer.prompt(ActionQuestions)
ActionAnswer = ActionAnswers["ActionType"]

if ActionAnswer == 'connect':
    # Call vpncli.exe session to connect
    subprocess.run([AnyConnectVpnCli, f'connect', HostNameAnswer, f'-s'])

    #Metric setup on the AnyConnect interface
    NetAdapterMetricQuestion = [
    inquirer.Confirm("MetricEdit", message="Do you want to set the Cisco AnyConnect adapter metric to value 100?", default=True),
    ]
    NetAdapterMetricAnswer = inquirer.prompt(NetAdapterMetricQuestion)

    if NetAdapterMetricAnswer["MetricEdit"] is True:
        print("You choosed Yes.")
        #PS command
        c = subprocess.run(["powershell", "Get-NetAdapter | Where-Object { $_.InterfaceDescription -like '*Cisco AnyConnect*' } | Set-NetIPInterface -InterfaceMetric 100"], stdout=sys.stdout)
        print ("Result: ", c)
        print("AnyConnect-Windows python script is telling goodbye :)")
    else:
        print("You choosed No")
        print("AnyConnect-Windows python script is telling goodbye:)")
elif ActionAnswer == 'disconnect':
    # Call vpncli.exe session to disconnect
    subprocess.run([AnyConnectVpnCli, f'disconnect', HostNameAnswer])
elif ActionAnswer == 'status':
    # Call vpncli.exe to show status
    subprocess.run([AnyConnectVpnCli, f'status', HostNameAnswer])
else:
    #Exception
    print("The action choice selected doesn't exist. Contact developer.")