# Keylogger


<!-- vim-markdown-toc GFM -->

* [Install evdev](#install-evdev)
* [Run keylogger](#run-keylogger)
* [Check event devices](#check-event-devices)
	* [By bash](#by-bash)
	* [By python3](#by-python3)

<!-- vim-markdown-toc -->

## Install evdev

`sudo pip3 install evdev`

## Run keylogger

`sudo python3 keylogger.py`

Because it's a keylogger, you are not able to kill it by Ctrl+C or Ctrl+D.Just close tty to kill it.

## Check event devices

If it shows "Can't find keyboard device!", you can use the following two ways to find where is your keyboard device.

Then you can use `device = InputDevice('/dev/input/eventX')` in line 50 to replace the function findDevice().

### By bash

`cat /proc/bus/input/devices`

For me,the keyboard is event3 as below

```
I: Bus=0011 Vendor=0001 Product=0001 Version=ab83
N: Name="AT Translated Set 2 keyboard"
P: Phys=isa0060/serio0/input0
S: Sysfs=/devices/platform/i8042/serio0/input/input3
U: Uniq=
H: Handlers=sysrq kbd event3 leds 
B: PROP=0
B: EV=120013
B: KEY=20000 20 0 0 1500f02100000 3803078f900d401 feffffdfffefffff fffffffffffffffe
B: MSC=10
B: LED=7
```

### By python3

You can also use evdev to show this
That's listEventDevices.py in this dir. Remember use `sudo` to run it.

```
import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for devs in devices:
    print(devs.path, devs.name, devs.phys)
```

The same result.
`/dev/input/event3 AT Translated Set 2 keyboard isa0060/serio0/input0`


