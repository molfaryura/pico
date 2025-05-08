import machine

import utime

pin = range(6, 16)

led = []

for i in range(10):
    led.append(None)
    led[i] = machine.Pin(pin[i], machine.Pin.OUT)

while True:
    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)
