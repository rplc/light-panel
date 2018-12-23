from gpiozero import PWMOutputDevice
from time import sleep

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

iterations = 20
increment = 1.0 / 20

for x in range(0, iterations):
    v = x * increment

    print(v)
    green.value = v
    red.value = v
    blue.value = v

    sleep(1)