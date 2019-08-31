import os
import bottle
import random
import json
import argparse
os.chdir(os.path.dirname(__file__))

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

def setup_routing(app):
    bottle.route("/{}".format(CONFIG['prefix']), ["GET"], forward)
    bottle.route("/{}/<id:int>".format(CONFIG['prefix']), ["GET"], forward)

def forward(id=None):
    if id is None:
        id=random.randint(0, len(targets)-1)

    bottle.redirect(targets[id], 302)


app = bottle.Bottle()
setup_routing(app)
