import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objs as go




price = pd.read_csv('https://raw.githubusercontent.com/prubinstreit/animated-plotly/master/df2.csv')
number = pd.read_csv('https://raw.githubusercontent.com/prubinstreit/animated-plotly/master/Group_means.csv')




app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H4('Animated Means by Donor Category and Ancestry over Date'),
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=["Price","IUI Number", "IUI ART Number", "ICI Number","ICI ART Number"],
        value="Price",
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(Output("graph", "figure"), Input("selection", "value"))
def display_animated_graph(selection):
    #data  # replace with your own data source
    animations = {
        "Price":
             px.bar(price,
               x="Ancestry",
               y='Mean',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group', range_y=[0,1500]),
        
        "IUI Number":
             px.bar(number,
               x="Ancestry",
               y= 'IUI Number',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'),  
        
        "IUI ART Number":
             px.bar(number,
               x="Ancestry",
               y= 'IUI ART Number',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'), 
        
        "ICI Number":
             px.bar(number,
               x="Ancestry",
               y= 'ICI Number',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'), 
        
        "ICI ART Number":
             px.bar(number,
               x="Ancestry",
               y= 'ICI ART Number',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group')         
        
    }
    return animations[selection]




if __name__ == '__main__':
    app.run_server()
