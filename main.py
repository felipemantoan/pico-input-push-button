from machine import Pin

pin15 = Pin(15, Pin.IN, Pin.PULL_DOWN)
pin25 = Pin(25, Pin.OUT)

while True:
    pin25.value(pin15.value())
    print(pin15.value())

