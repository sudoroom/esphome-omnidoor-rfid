#!/opt/python-3.9/bin/python3

import aioesphomeapi
import asyncio
import os
from datetime import datetime

CLIENT_ADDRESS = "omni-door-sudo.local"
CLIENT_PASSWORD = "shealing duarchy sorrowy welsium"

print("Content-type: text/html\n")

print("<html>")

username=os.environ['REMOTE_USER']
# https://strftime.org/
print(datetime.now().strftime("%a %b %H:%M:%S %Z %Y ")+username+" open-sudo-door.py")
logfile.write(datetime.now().strftime("%a %b %H:%M:%S %Z %Y ")+username+" open-sudo-door.py")

print("<p>Welcome, {}. Time={}".format(username, datetime.now()))
#for key,val in os.environ.items():
#    print("<p>%s=%s</p>" % (key, val))

# pip3 install aioesphomeapi
async def main():
   """Connect to an ESPHome device and get details."""

   # Establish connection 
   api = aioesphomeapi.APIClient(CLIENT_ADDRESS, 6053, CLIENT_PASSWORD)
   await api.connect(login=True)
   
   # Get API version of the device's firmware
   print(api.api_version)
   
   # Show device details
   device_info = await api.device_info()
   print(device_info)
   
   # List all entities of the device
   sensors, services = await api.list_entities_services()
   print("<p>sensors: {}</p>\n<p>services: {}</p>".format(sensors,services))

   unlockdoor = aioesphomeapi.UserService(name='unlock_door', key=2199959000, args=[])
   print("<p>unlockdoor: {}</p>".format(unlockdoor))

   print("<p>unlock_door</p>")
   ul = await api.execute_service(unlockdoor,[])
   
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("</html>")

