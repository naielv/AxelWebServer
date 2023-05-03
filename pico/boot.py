## DELETE THIS FILE TO USE CUSTOM CODE ##
import urequests
r = urequests.request("GET", "https://github.com/naielv/AxelWebServer/releases/latest/download/files.json")
with open("files.json", "w") as f:
    f.write(r.text)