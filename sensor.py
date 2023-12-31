import evdev
from evdev import categorize, ecodes
import requests
import subprocess


class Device():
    name = 'Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader'

    @classmethod
    def list(cls, show_all=False):
        # list the available devices
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        if show_all:
            for device in devices:
                print("event: " + device.fn, "name: " + device.name, "hardware: " + device.phys)
        return devices

    @classmethod
    def connect(cls):
        # connect to device if available
        try:
            device = [dev for dev in cls.list() if cls.name in dev.name][0]
            device = evdev.InputDevice(device.fn)
            return device
        except IndexError:
            print("Device not found.\n - Check if it is properly connected. \n - Check permission of /dev/input/ (see README.md)")
            exit()

    @classmethod
    def run(cls):
        try:
            device = cls.connect()
            container = []
            try:
                device.grab()
                # bind the device to the script
                print("RFID scanner is ready....")
                print("Press Control + c to quit.")
                for event in device.read_loop():
                        # enter into an endeless read-loop
                        if event.type == ecodes.EV_KEY and event.value == 1:
                            digit = evdev.ecodes.KEY[event.code]
                            if digit == 'KEY_ENTER':
                                # create and dump the tag
                                tag = "".join(i.strip('KEY_') for i in container)
                                print(tag)
                                val = requests.post(
                                "http://localhost:5000/checkCard", 
                                data=None,
                                json={'cardId':tag}
                                )
                                container = []
                            else:
                                container.append(digit)

            except Exception as e:
                # catch all exceptions to be able release the device
                print(e)
                device.ungrab()
                print('Quitting.')
        except :
            subprocess.Popen('python3 sensor2.py', shell=True)

Device.run()