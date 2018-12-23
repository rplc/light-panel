from gpiozero import PWMOutputDevice
from time import sleep
import signal

def signal_handler(sig, frame):
    green.close()
    red.close()
    blue.close()
signal.signal(signal.SIGINT, signal_handler)

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

iterations = 20
increment = 1.0 / 20

print("init done")

for x in range(0, iterations):
    v = x * increment

    print(v)
    green.value = v
    red.value = v
    blue.value = v

    sleep(1)

green.close()
red.close()
blue.close()