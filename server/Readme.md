# Wiring

# Software Setup
- sudo apt-get install python3 python3-dev ipython3 python3-pip python3-gpiozero bluetooth libbluetooth-dev
- sudo pip3 install pybluez
- modifying /etc/systemd/system/dbus-org.bluez.service add -C to ExecStart=/usr/lib/bluetooth/bluetoothd
- sudo sdptool add SP

# UDP Commands#
- Port 5445
- origin only from the same network
{
    'cmd': 'setColor',
    'arg': '#000'
}
{
    'cmd': 'shutdown'
}