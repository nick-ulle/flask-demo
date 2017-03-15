
import bokeh, bokeh.charts
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
import requests


def fetch():
    response = requests.get("https://api.github.com/events")
    response.raise_for_status()

    return response.json()


def parse_events(events):
    data = (
        (evt['type'], evt['actor']['login'], evt['repo']['name'])
        for evt in events
    )

    return pd.DataFrame.from_records(data, columns = ["Type", "User", "Repo"])


def bar_plot_types(events):
    plot = bokeh.charts.Bar(events, "Type")

    return bokeh.embed.components(plot)
