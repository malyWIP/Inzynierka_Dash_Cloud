import dash
import dash_core_components as dcc
import dash_html_components as html


#########################
# Dashboard Layout / View
#########################


app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True
app.layout = html.Div([
    html.Div([
        html.Button('Start', id='Start', n_clicks_timestamp='0'),
        html.Button('Stop', id='Stop', n_clicks_timestamp='0'),
        html.Div(id='container')
    ]),
    html.Div([
        html.H1("System nadzorowania pracy gniazda produkcyjnego Industry 4.0"),

        html.Div(id='result'),
        dcc.Graph(id='live-update-graph-scatter', animate=False),
        # dcc.Graph(id='live-update-graph-bar'),
        dcc.Interval(
            id='interval-component',
            interval=200,
            disabled=False


        )
    ]),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='dropdown-interval-control',
                options=[
                    {'label': 'No Updates', 'value': 'no'},
                    {'label': 'Slow Updates', 'value': 'slow'},
                    {'label': 'Regular Updates', 'value': 'regular'},
                    {'label': 'Fast Updates', 'value': 'fast'}
                ],
                value='regular',
                className='ten columns',
                clearable=False,
                searchable=False
            ),
            ]),
        dcc.Interval(
            id="interval-log-update",
            n_intervals=0
        ),
    ]),
])