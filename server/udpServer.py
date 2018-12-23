import socket
import json
import signal
import lightpanel
import sys

def signal_handler(sig, frame):
    lightpanel.shutdown()
signal.signal(signal.SIGINT, signal_handler)

UDP_IP = ""
UDP_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)

    try:
        payload = json.loads(data.decode())
        cmd = payload["cmd"]

        if cmd == "setColor":
            lightpanel.setColor(payload["arg"])
            print("setColor to", payload["arg"])

        elif cmd == "shutdown":
            lightpanel.shutdown()
            print("shutdown received")
            break #break the while true loop
    except:
        print("exception triggered")
        pass
