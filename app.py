from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Animated Mean IUI Price by Donor Category and Ancestry'),
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=["Population - Bar"],
        value='Population - Bar',
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(Output("graph", "figure"), Input("selection", "value"))
def display_animated_graph(selection):
    df2  # replace with your own data source
    animations = {
        # 'GDP - Scatter': px.scatter(
        #     df, x="gdpPercap", y="lifeExp", animation_frame="year",
        #     animation_group="country", size="pop", color="continent",
        #     hover_name="country", log_x=True, size_max=55,
        #     range_x=[100,100000], range_y=[25,90]),
        'Population - Bar':
        px.bar(df2,
               x="Ancestry",
               y='Mean',
               color="Donor Category",
               animation_frame="Date",
               animation_group="Ancestry",
               barmode='group'),
    }
    return animations[selection]




if __name__ == '__main__':
    app.run_server()
