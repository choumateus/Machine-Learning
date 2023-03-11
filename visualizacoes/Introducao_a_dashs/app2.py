import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(id = "div1",
    children=[
        html.H1("Hello Dash", id = "h1", style = {"color":"#FF00FF"}),

    html.Div("Dash : framework de front do python"),

    ]
)
if __name__ == '__main__':
    app.run_server(debug = True)
