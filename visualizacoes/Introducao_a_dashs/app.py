import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc

app = dash.Dash(__name__)

df = px.data.iris()

fig = px.scatter(df, x = "sepal_length", y = "sepal_width", color="species")

app.layout = html.Div(id = "div1",
    children=[
        html.H1("Hello Dash", id = "h1"),

    html.Div("Dash : framework de front do python"),

    dcc.Graph(figure = fig, id = "graph")
    ]
)
if __name__ == '__main__':
    app.run_server(debug = True)
