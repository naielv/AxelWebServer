from machine import Pin
import network
import time

try:
    import usocket as socket
except:
    import socket
from secrets import SSID, PASS

l = open("files.json", "r")

DATA = l.read()
FILE = eval(DATA)


l.close()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASS)  # ssid, password

# connect the network
wait = 15
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


def web_server(file: str):
    files = FILE
    page = str(dict(files).get(file))
    if page == None:
        return str(dict(files).get("404"))
    return page


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print("Got a connection from %s" % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        file = request.split("\\r\\n")[0].split(" ")[1]
        print("File: " + file)
        response = web_server(file)
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print("Connection closed")
