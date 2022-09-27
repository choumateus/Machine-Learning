import pandas as pd
import plotly.express as px
import dash
from dash import html

app = dash.Dash(__name__)

df = px.data.iris()

fig = px.scatter(df, x = "sepal_length", y = "sepal_width", color="species")

app.layout = html.Div(
    id = "div1"
    children=
[
    html.H1("Hello Dash", id = "h1")

    html.Div()
]
)