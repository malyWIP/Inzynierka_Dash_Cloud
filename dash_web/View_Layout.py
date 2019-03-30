import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

#########################
# Dashboard Layout / View
#########################


def get_logo():
    image = r'D:\STUDIA\Inżynierka\Dash_App\images\dash-logo-stripe.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image\png;base64,{}".format(encoded_image.decode()), height="100"
        ),
        style={"marginTop": "0"},
        className="sept columns",
    )
    return logo


app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True
app.layout = html.Div([
    get_logo(),
    html.Div([
        html.Button('Start', id='Start', n_clicks='0'),
        html.Button('Stop', id='Stop', n_clicks='0'),
        html.Div(id='container')
    ]),
    html.Div([
        html.H1("System nadzorowania pracy gniazda produkcyjnego Industry 4.0"),

        html.Div(id='result'),
        html.Div(id='edge-sharpness'),
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


