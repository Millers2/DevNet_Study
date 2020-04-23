"""
Some lines are commented out.
You may or may not want to use the ipaddress library
but you will still need to check for a valid IPv4 adddress.

The 'with open('JSONdata') as f:' line will read the data file
AS LONG AS IT IS IN THE SAME DIRECTORY :)

The next line should get you started with a method you will need
from the json library to change the JSON text into something 
you can call from Python
"""


#import ipaddress
import json
import ipaddress

#Open JSON file
with open('C:\ScottM\Python\DevNetStudy_Challenge3\DevNetStudy_Challenge3\JSONdata') as f:
    data = json.load(f)
    
    #Parse file
    for NetObject in data:
        ip = NetObject['lanIp']
        serial = NetObject['serial']
        
        #Confirm valid IP, Error out if not.
        try:
            ipaddress.IPv4Address(ip)
            print('{} is a Valid IP Address for Serial {}'.format(ip, serial))        
        except ValueError:
            print('{} is NOT a Valid IP Address for Serial {}'.format(ip, serial))
