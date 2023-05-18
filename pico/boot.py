import network
import time
from secrets import SSID, PASS

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASS)  # ssid, password

# connect the network
wait = 30
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print("waiting for connection...")
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError("wifi connection failed")
else:
    print("connected")
    ip = wlan.ifconfig()[0]
    print("IP: ", ip)

