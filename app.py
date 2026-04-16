from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_sales_data.csv')

df = df.sort_values(by='date')

app = Dash(__name__)

fig = px.line(
    df, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales (Highlighting Jan 15, 2021 Price Increase)',
    labels={'sales': 'Sales Revenue ($)', 'date': 'Date'}
)

app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods: Pink Morsel Sales Visualizer", 
            className="header-title"
        ),
        dcc.Graph(
            id='sales-line-chart',
            figure=fig
        )
    ],
    className="app-container"
)

if __name__ == '__main__':
    app.run(debug=True)