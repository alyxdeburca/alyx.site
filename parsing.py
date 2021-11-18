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
table = """
                        </p>
                    </div>
                </div>
			    <div class="col-md-2">
				    <div class="card-body">
					    <p class="card-text">""".join(inv_dict)
html = """
<html>
<head>
<!-- Main Stylesheet -->
<link rel="stylesheet"  type="text/css" href="styles/main.css">
<!-- Google Fonts Stylesheet -->
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Tangerine">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<div class="container-fluid">
	<div class="row">
		<div class="col-md-12">
			<h3 class="text-center text-info">
				<a href="https://steamcommunity.com/id/csalyx/inventory/730">Alyx's CS:GO Inventory</a>
			</h3>
			<div class="row">
				<div class="col-md-2">
					<div class="card-body">
						<p class="card-text">
""" + table + """
                </p>
			</div>
		</div>
	</div>
</div>

</html>"""
f.write(html)
