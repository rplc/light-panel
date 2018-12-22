from gpiozero import PWMOutputDevice
import time
import random

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

while True:
    green.value = random.uniform(0, 1.0)
    red.value = random.uniform(0, 1.0)
    blue.value = random.uniform(0.0, 1.0)

    time.sleep(1000)