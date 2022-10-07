#!/usr/bin/env python3
# pip3 install aioesphomeapi
# https://github.com/esphome/aioesphomeapi

CLIENT_ADDRESS = "omni-door-sudo.local"
CLIENT_PASSWORD = "shealing duarchy sorrowy welsium"

import aioesphomeapi
import asyncio

async def main():
   """Connect to an ESPHome device and get details."""

   # Establish connection 
   api = aioesphomeapi.APIClient(CLIENT_ADDRESS, 6053, CLIENT_PASSWORD)
   await api.connect(login=True)
   
   # Get API version of the device's firmware
   # print(api.api_version)
   
   # Show device details
   # device_info = await api.device_info()
   # print(device_info)
   
   # List all entities of the device
   # sensors, services = await api.list_entities_services()
   # print("sensors: ",sensors)
   # print("services: ",services)

   unlockdoor = aioesphomeapi.UserService(name='unlock_door', key=2199959000, args=[])
   # print("unlockdoor: ",unlockdoor)

   print("unlock_door")
   ul = await api.execute_service(unlockdoor,[])
   
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

