import qrcode
import json
import os

# Config
CONFIG = {
        "linkfile": "links.json",
        "prefix": "q"
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

for i, link in enumerate(targets):
    img = qrcode.make(link)
    img.save("qr-codes/{}.png".format(i), "png")
