import machine

import utime

button = machine.Pin(14, machine.Pin.IN)

while True:
    if button.value() == 0:
        print("The switch works!")
        utime.sleep(1)
        print("\033[H\033[J", end="")
    else:
        print("The switch is off.")
        utime.sleep(1)
        print("\033[H\033[J", end="")
