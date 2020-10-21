import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for devs in devices:
    print(devs.path, devs.name, devs.phys)
