from dash import Dash, html, dash_table, dcc, callback, Output, Input
# dcc(Dash Core Component) : Make a Component to render interactive graphs, or figures.
import pandas as pd
import plotly.express as px
#import dash_mantine_components as dmc

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

app = Dash()

app.layout = [  # On layout, dash components can be inserted
        html.Div(children="Hello World"),
        html.Hr(),
        dcc.RadioItems(options=["pop", "lifeExp", "gdpPercap"], value="lifeExp", id="control-and-radio-item"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=6),
        dcc.Graph(figure={}, id="control-and-graph")   # Empty Component can be made with {}
    ]   # As a parameter of dash components other objects from plotly and dataframe can be inserted.

@callback(#Register Event and connect to the component as a event
    Output(component_id="control-and-graph", component_property="figure"),# Event out to Component
    Input(component_id="control-and-radio-item", component_property="value")# Event read from Component
    )
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig

if __name__=="__main__":
    app.run(debug=True)


