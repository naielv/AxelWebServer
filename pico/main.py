from machine import Pin
import time

try:
    import usocket as socket
except:
    import socket
from secrets import SSID, PASS
import urequests
def FILE():
    l = open("files.json", "r")
    DATA = l.read()
    FILE = eval(DATA)
    l.close()
    return FILE
def update():
    r = urequests.request("GET", "https://github.com/naielv/AxelWebServer/releases/latest/download/files.json")
    l = open("files.json", "w")
    l.write(r.text)
    l.close()
def web_server(file: str):
    files = FILE()
    page = str(dict(files).get(file))
    if file == "/_update":
        print("Updating")
        update()
    if page == "None":
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

