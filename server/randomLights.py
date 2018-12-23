from gpiozero import PWMOutputDevice
from time import sleep
from random import uniform
import signal

def signal_handler(sig, frame):
    green.close()
    red.close()
    blue.close()
signal.signal(signal.SIGINT, signal_handler)

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

print("init done")

while True:
    green.value = uniform(0, 1.0)
    red.value = uniform(0, 1.0)
    blue.value = uniform(0, 1.0)

    sleep(1)