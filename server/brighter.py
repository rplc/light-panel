from gpiozero import PWMOutputDevice
import time

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

iterations = 20
increment = 1.0 / 20


for x in range(0, 20)
    v = x * increment

    green.value = v
    red.value = v
    blue.value = v

    time.sleep(1000)