#from dash import Input, Output
import plotly.express as px
import pandas as pd

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go



price = pd.read_csv('https://raw.githubusercontent.com/prubinstreit/animated-plotly/master/df2.csv')
number = pd.read_csv('https://raw.githubusercontent.com/prubinstreit/animated-plotly/master/df_IUI_number.csv')


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
server = app.server
#selection = 'Population - Bar'
app.layout = html.Div([
    html.H4('Mean IUI Price by Donor Category and Ancestry Animated over Date'),
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=["price","number"],
        value='number',
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(Output("graph", "figure"), Input("selection", "value"))
def display_animated_graph(selection):
    #data  # replace with your own data source
    animations = {
        'Population - Bar':
             px.bar(selection,
               x="Ancestry",
               y='Mean',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'),
    }
    return animations[selection]

#display_animated_graph


if __name__ == '__main__':
    app.run_server()
