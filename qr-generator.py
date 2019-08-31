import qrcode
import json
import os

# Config
CONFIG = {
        "linkfile": "links.json",
        "server": "https://noerdcampus.de/avatar/q"
        }


# Import questions

with open(CONFIG['linkfile'], 'r') as lf:
    linkfilecontents = json.load(lf)

assert "list" in linkfilecontents
targets = linkfilecontents['list']

try:
    os.mkdir("qr-codes")
except FileExistsError as e:
    pass


img = qrcode.make("{}".format(CONFIG['server']))
img.save("qr-codes/random.png", "png")
for i, link in enumerate(targets):
    img = qrcode.make("{}/{}".format(CONFIG['server'], i))
    img.save("qr-codes/{}.png".format(i), "png")
