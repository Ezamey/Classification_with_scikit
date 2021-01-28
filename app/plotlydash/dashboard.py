"""Instantiate a Dash app."""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/css/main.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )
         
    # Load DataFrame
    df = pd.read_csv("app\Datasets\Modified\mod_UCI_Credit_Card.csv")

    tab = generate_table(df)

    # Create Layout
    dash_app.layout = html.Div(
        children=[html.A("Back",href="/index"),
                html.H3(children = "A quick raw overview of the dataset"),
                tab],
        id="dash-container"
    )
    return dash_app.server

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
