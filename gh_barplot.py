
import flask
from flask import Flask

import gh_events


app = Flask(__name__)


@app.route("/")
def index():
    events = gh_events.fetch()
    events = gh_events.parse_events(events)
    script, div = gh_events.bar_plot_types(events)
    return flask.render_template("index.html", script = script, div = div)


@app.route("/hello<int:n>")
def hello(n):
    if n == 1:
        return "Hello, world!"
    else:
        return "Hello, all {} worlds!".format(n)
