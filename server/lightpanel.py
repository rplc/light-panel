from gpiozero import PWMOutputDevice
from time import sleep

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

def setColor(hexColor):
    hexColor = hexColor.lstrip('#')
    (r, g, b) = tuple(int(hexColor[i:i+2], 16) for i in (0, 2 ,4))
    green.value = g/255
    red.value = r/255
    blue.value = b/255

def shutdown():
    setColor('#000000')
    sleep(0.05)
    green.close()
    red.close()
    blue.close()