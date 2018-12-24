# Wiring

# Software Setup

## Bluetooth
- `sudo apt-get install bluetooth libbluetooth-dev`
- `sudo pip3 install pybluez`
- modifying `/etc/systemd/system/dbus-org.bluez.service` add -C to `ExecStart=/usr/lib/bluetooth/bluetoothd`
- `sudo sdptool add SP`

## GPIO
- `sudo apt-get install python3 python3-dev ipython3 python3-pip python3-gpiozero`

# Commands
- Port 5445
- origin only from the same network
```bash
{
    'cmd': 'setColor',
    'arg': '#000'
}
{
    'cmd': 'shutdown'
}
```