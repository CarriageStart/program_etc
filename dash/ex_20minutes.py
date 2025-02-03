from dash import Dash, html, dash_table, dcc
# dcc(Dash Core Component) : Make a Component to render interactive graphs, or figures.
import pandas as pd
import plotly.express as px
#import dash_mantine_components as dmc

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

app = Dash()

app.layout = [  # On layout, dash components can be inserted
        html.Div(children="Hello World"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg"))
    ]   # As a parameter of dash components other objects from plotly and dataframe can be inserted.

if __name__=="__main__":
    app.run(debug=True)


