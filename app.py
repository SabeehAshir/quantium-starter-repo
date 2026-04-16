from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('formatted_sales_data.csv')
df = df.sort_values(by='date')


app = Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods: Pink Morsel Sales Visualizer", 
            className="header-title"
        ),
        
        html.Div(
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all', 
                className="radio-group"
            ),
            className="region-selector"
        ),
        
        dcc.Graph(
            id='sales-line-chart'
        )
    ],
    className="app-container"
)

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title=f'Pink Morsel Sales ({selected_region.capitalize()} Region)',
        labels={'sales': 'Sales Revenue ($)', 'date': 'Date'}
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)