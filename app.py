#from dash import Input, Output
import plotly.express as px
import pandas as pd

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go



price = pd.read_csv('https://raw.githubusercontent.com/prubinstreit/animated-plotly/master/df2.csv')
number = pd.read_csv('https://raw.githubusercontent.com/prubinstreit/animated-plotly/master/Group_means.csv')


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
server = app.server
#selection = 'Population - Bar'
app.layout = html.Div([
    html.H4('Mean IUI Data by Donor Category and Ancestry Animated over Date'),
    html.P("Select a Variable:"),
    dcc.RadioItems(
        id="selection",
        options=["Price","IUI Number", ,"IUI ART Number", "ICI Number","ICI ART Number"],
        value="Price", 
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])



@app.callback(Output("graph", "figure"), Input("selection", "value"))

def display_animated_graph(selection):
    animations = {
        "Price":
             px.bar(price,
               x="Ancestry",
               y='Mean',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'),

          'Number':
             px.bar(number,
               x="Ancestry",
               y= selection,
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'),        
    }
    return animations[selection]

#display_animated_graph


if __name__ == '__main__':
    app.run_server()
