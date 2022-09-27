import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# Dash App com múltiplos inputs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = px.data.iris()
corr = df.corr('pearson')

available_indicators = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
species_p = df['species'].unique().tolist()
species_p.append('all')
species_p.sort()

app.layout = html.Div([
    html.Div([

        html.Div([
            html.Label("eixo x", className="label"),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='sepal_length'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            html.Label("eixo y", className="label"),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='sepal_width'
            )

        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

        html.Div([
            html.Label("espécie", className="label"),
            dcc.Dropdown(
                id='species',
                options=[{'label': i, 'value': i} for i in species_p],
                value = species_p[0]
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
]),
    html.H3(id = 'values-est'),
    dcc.Graph(id='indicator-graphic'),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('species', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, specie):
    if specie == 'all':
        fig = px.scatter(df, x=xaxis_column_name,
            y=yaxis_column_name, color = 'species')
    else:
        fig = px.scatter(df[df['species'] == specie], x=xaxis_column_name,
            y=yaxis_column_name, color = 'species')


    # fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    
    return fig

@app.callback(
    Output('values-est', 'children'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('species', 'value')])
def update_val(xaxis_column_name, yaxis_column_name, specie):
    if specie == 'all':
        texto = "coeficiente de correlação = " + str(corr[xaxis_column_name][yaxis_column_name])
    else:
        corr2 = df[df['species'] == specie].corr('pearson')
        texto = "coeficiente de correlação = " + str(corr2[xaxis_column_name][yaxis_column_name])
    # texto = "coeficiente de correlação = " + str(corr[xaxis_column_name][yaxis_column_name])
    return texto


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)