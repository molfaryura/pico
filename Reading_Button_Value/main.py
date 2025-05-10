import machine

import utime

button = machine.Pin(14, machine.Pin.IN)

while True:
    if button.value() == 0:
        print("Button pressed!")
        utime.sleep(1)
    else:
        print("Button not pressed")
        utime.sleep(1)
