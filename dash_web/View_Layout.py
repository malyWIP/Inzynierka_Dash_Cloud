import dash
import dash_core_components as dcc
import dash_html_components as html
import base64
import dash_bootstrap_components as dbc
#########################
# Dashboard Layout / View
#########################


def get_logo_dash():
    image = r'D:\STUDIA\Inżynierka\Dash_App\images\dash-logo-stripe.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image\png;base64,{}".format(encoded_image.decode()), height="50"
        ),
        style={"marginTop": 0},
        className="sept columns",
    )
    return logo

def get_logo_dash_WIP():
    image = r'D:\STUDIA\Inżynierka\Dash_App\images\WIP_Znak.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image\png;base64,{}".format(encoded_image.decode()), height="148", width='736'
        ),
        style={"marginTop": "50", 'textAlign': 'center'},
        className="sept columns",
    )
    return logo


def get_logo_dash_industry():
    image = r'D:\STUDIA\Inżynierka\Dash_App\images\industry_4.0.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image\png;base64,{}".format(encoded_image.decode()), height="100", width='400'
        ),
        style={"marginTop": "100", 'textAlign': 'center'},
        className="sept columns",

    )
    return logo


def get_logo_dash_press():
    image = r'D:\STUDIA\Inżynierka\Dash_App\images\power_press.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image\png;base64,{}".format(encoded_image.decode()), height="400", width='380'
        ),
        style={"marginTop": 0, 'textAlign': 'center'},
        className="sept columns",

    )
    return logo
#
external_stylesheets = [dbc.themes.BOOTSTRAP,'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions']=True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    get_logo_dash(),
    get_logo_dash_WIP(),
    html.Br(),
    html.Div(html.H2('Instytut Technik Wytwarzania'),style={"marginTop": 250, 'textAlign': 'center', 'color': '#000066', 'size': 200}),
    html.Div(
        html.H1('System nadzorowania pracy gniazda produkcyjnego'),
        style={"marginTop": 50, 'textAlign': 'center', 'color': '#000066', 'size': 200},
    ),
    get_logo_dash_industry(),
    html.Div(
        dcc.Link('Proces Wykrawania : Parametry', style={'color': '#b30059'}, href='/page-1'),
        style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
        dcc.Link('Analiza procesu wykrawania ', style={'textAlign': 'right', 'color': '#b30059'}, href='/page-2'),
        style={"marginRight": 100,'textAlign': 'right'}
    )
])

page_1_layout = html.Div([
    html.Div(
        html.H1('Proces Wykrawania : Parametry'),
        style={'color': '#000066', 'textAlign': 'center'}),
    html.Div([
        html.Button('Start', id='Start', n_clicks='0'),
        html.Button('Stop', id='Stop', n_clicks='0'),
        html.Button('Reset', id='Reset', n_clicks='0'),
        html.Div(id='container')
    ]),
    html.Div([
        html.H1("System nadzorowania pracy gniazda produkcyjnego Industry 4.0"),

        html.Div(id='result'),
        html.Div(id='edge-sharpness'),
        html.Div(id='Process_Parameters'),
        dcc.Graph(id='live-update-graph-scatter', animate=False,  ),
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
    html.Div(id='page-1-content'),
    html.Br(),
    html.Div(
            dcc.Link('Analiza procesu wykrawania', style={'color': '#b30059'}, href='/page-2'),
            style={"marginRight": 100,"marginTop": 50,'textAlign': 'right'}),
    html.Div(
            dcc.Link('Strona główna', style={'textAlign': 'right', 'color': '#b30059'}, href='/'),
            style={"marginRight": 100,'textAlign': 'right'}
        )
])

page_2_layout = html.Div([
    html.H1('Analiza procesu wykrawania '),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    html.Div(
            dcc.Link('Proces Wykrawania : Parametry', style={'color': '#b30059'}, href='/page-1'),
            style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
            dcc.Link('Strona główna', style={'textAlign': 'right', 'color': '#b30059'}, href='/'),
            style={"marginRight": 100,'textAlign': 'right'}
        )
])
