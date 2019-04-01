import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'background2': '#FF0',
    'text': '#7FDBFF'
}

app.layout = html.Div( children = [
        html.Div([
            html.H5('ANNx'),
            dcc.Graph(
                id='cx1'
                )

        ])
    ]
)


@app.callback(Output('cx1', 'figure'))

def update_figure( ):
    return  {
                    'data': [
                        {'x': ['APC'], 'y': [9], 'type': 'bar', 'name': 'APC'},
                        {'x': ['PDP'], 'y': [8], 'type': 'bar', 'name': 'PDP'},
                    ],
                    'layout': {
                        'title': 'Basic Dash Example',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background']
                    }
                    }


# if __name__ == '__main__':
#     app.run_server(debug=True)