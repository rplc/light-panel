from gpiozero import PWMOutputDevice

green = PWMOutputDevice(16)
red = PWMOutputDevice(20)
blue = PWMOutputDevice(21)

def setColor(hexColor):
    hexColor = hexColor.lstrip('#')
    (red, green, blue) = tuple(int(hexColor[i:i+2], 16) for i in (0, 2 ,4))
    green.value = green/255
    red.value = red/255
    blue.value = blue/255

def shutdown():
    setColor('#000000')
    green.close()
    red.close()
    blue.close()