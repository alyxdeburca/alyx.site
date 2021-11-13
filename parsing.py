from json import loads
from os import remove
import urllib.request
url = "http://steamcommunity.com/id/csalyx/inventory/json/730/2"
data = urllib.request.urlopen(url).read().decode()
inv = loads(data)
inv_dict = []
for item in inv["rgDescriptions"]:
    inv_dict.append(inv["rgDescriptions"][item]["name"])

f = open("cs.html", "w")
table = "</br>".join(inv_dict)
html = """
<html> 
<p>""" + table + """
</p></html>"""
f.write(html)
