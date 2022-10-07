
Config file for prototype ESPHome ESP32 device to control the ccl/sudo door in CCL using RFID.

Beware that a password is contained in the yml file. You should change it before using this in production.
                                                                ^^^^^ lol you mean so hackers don't get in? :)

To compile and run first install [esphome](https://esphome.io/) (Python >= 3.7 required):

```
pip3 install esphome
```

Then compile and upload:

```
esphome compile omni_door.yml
esphome upload omni_door.yml
```

Now in home-assistant add your new esphome node (it will probably be auto-discovered). Then scan a tag and go to the tag manager and give it a name. Set up an automation. The trigger should be of type Tag and the Tag should be the name of the tag you just names. The action should be "esphome.omni_door_sudo_unlock_door".

That's it.
