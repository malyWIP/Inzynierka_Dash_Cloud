import dash
import dash_core_components as dcc
import dash_html_components as html
import base64
import dash_bootstrap_components as dbc
import flask
#########################
# Dashboard Layout / View
#########################


def get_logo_dash():
    image = r'images/dash-logo-stripe.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image/png;base64,{}".format(encoded_image.decode()), height="50"
        ),
        style={"marginTop": 0},
        className="sept columns",
    )
    return logo

def get_logo_dash_WIP():
    image = r'images/WIP_Znak.png'
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
    image = r'images/industry_4.0.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image/png;base64,{}".format(encoded_image.decode()), height="100", width='400'
        ),
        style={"marginTop": "100", 'textAlign': 'center'},
        className="sept columns",

    )
    return logo


def get_logo_dash_press():
    image = r'images/power_press.png'
    encoded_image = base64.b64encode(open(image, "rb").read())
    logo = html.Div(
        html.Img(
            src="data:image/png;base64,{}".format(encoded_image.decode()), height="400", width='380'
        ),
        style={"marginTop": 0, 'textAlign': 'center'},
        className="sept columns",

    )
    return logo
#
external_stylesheets = [dbc.themes.BOOTSTRAP,'https://codepen.io/chriddyp/pen/bWLwgP.css']
server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,server=server)
app.config['suppress_callback_exceptions']=True
server = app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# style={'fontSize': '16'} dziala w headerach
index_page = html.Div([
    get_logo_dash(),
    get_logo_dash_WIP(),
    html.Br(),
    html.Div(html.H2('Instytut Technik Wytwarzania'),style={"marginTop": 150, 'textAlign': 'center', 'color': '#000066'}),
    html.Div(
        html.H1('System nadzorowania pracy gniazda produkcyjnego'),
        style={"marginTop": 50, 'textAlign': 'center', 'color': '#000066', 'size': 200},
    ),
    get_logo_dash_industry(),
    html.Div(
        dcc.Link('Proces Wykrawania : Parametry', style={'color': '#b30059'}, href='/page-1'),
        style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
        dcc.Link('Analiza procesu wykrawania Strefa I oraz II', style={'textAlign': 'right', 'color': '#b30059'}, href='/page-2'),
        style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
        dcc.Link('Analiza procesu wykrawania Strefa III oraz IV ', style={'textAlign': 'right', 'color': '#b30059'}, href='/page-3'),
        style={"marginRight": 100, 'textAlign': 'right'}),
    html.Div(
        html.A("Powrót do CODESYS", href='http://192.168.1.2:8080/webvisu.htm', target="_blank",
               style={'textAlign': 'right', 'color': '#b30059'}),
        style={"marginRight": 100, 'textAlign': 'right'}
    )
])

page_1_layout = html.Div([
    html.Div(
        html.H1('Proces Wykrawania : Parametry',style={'color': '#000066', 'textAlign': 'center', 'size': 200}
        )),
    html.Div([
        html.Button('Start', id='Start', type='submit'),
        html.Button('Stop', id='Stop', type='submit'),
        html.Button('Reset', id='Reset', type='submit'),
        html.Div(id='container')
    ]),
    html.Div([
        html.Div(id='Process_Parameters'),
        html.Br(),
        html.Div(
            html.H1('Wyniki Analizy pracy ostrza w poszczególnych strefach' ,style={'color': '#000066', 'textAlign': 'center', 'size': 100}),
           ),
        html.Div(id='edge-sharpness'),
        html.Br(),
        html.Div(id='edge-sharpness-final'),
        dcc.Graph(id='live-update-graph-scatter', animate=False,  )
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
                value='fast',
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
            dcc.Link('Strona główna', style={'textAlign': 'right', 'color': '#b30059'}, href='/'),
            style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
            dcc.Link('Analiza procesu wykrawania Strefa I oraz II', style={'color': '#b30059'}, href='/page-2'),
            style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
        dcc.Link('Analiza procesu wykrawania Strefa III oraz IV ', style={'textAlign': 'right', 'color': '#b30059'},
                 href='/page-3'),
        style={"marginRight": 100, 'textAlign': 'right'}),
    html.Div(
        html.A("Powrót do CODESYS", href='http://192.168.1.2:8080/visu.htm', target="_blank", style={'textAlign': 'right', 'color': '#b30059'}),
        style={"marginRight": 100, 'textAlign': 'right'}
    )

])

page_2_layout = html.Div([
    html.H1('Analiza procesu wykrawania Srefa I oraz II '),
    html.Div([
        dcc.Graph(id='live-update-graph-scatter1', animate=False,  ),
        dcc.Graph(id='live-update-graph-scatter2', animate=False,  ),
        dcc.Graph(id='live-update-graph-scatter3', animate=False,  )
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
                value='fast',
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
    html.Div(id='page-2-content'),
    html.Br(),
    html.Div(
        dcc.Link('Strona główna', style={'textAlign': 'right', 'color': '#b30059'}, href='/'),
        style={"marginRight": 100, 'textAlign': 'right'}),
    html.Div(
            dcc.Link('Proces Wykrawania : Parametry', style={'color': '#b30059'}, href='/page-1'),
            style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
        dcc.Link('Analiza procesu wykrawania Strefa III oraz IV ', style={'textAlign': 'right', 'color': '#b30059'},
                 href='/page-3'),
        style={"marginRight": 100, 'textAlign': 'right'}),
    html.Div(
        html.A("Powrót do CODESYS", href='http://192.168.1.2:8080/webvisu.htm', target="_blank",
               style={'textAlign': 'right', 'color': '#b30059'}),
        style={"marginRight": 100, 'textAlign': 'right'}
    )
])

page_3_layout = html.Div([
    html.H1('Analiza procesu wykrawania Strefa III oraz IV'),
    html.Div([
        dcc.Graph(id='live-update-graph-scatter4', animate=False,  ),
        dcc.Graph(id='live-update-graph-scatter5', animate=False,  ),
        dcc.Graph(id='live-update-graph-scatter6', animate=False,  )
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
                value='fast',
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
    html.Div(id='page-3-content'),
    html.Br(),
    html.Div(
            dcc.Link('Strona główna', style={'textAlign': 'right', 'color': '#b30059'}, href='/'),
            style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
            dcc.Link('Proces Wykrawania : Parametry', style={'color': '#b30059'}, href='/page-1'),
            style={"marginRight": 100,'textAlign': 'right'}),
    html.Div(
        dcc.Link('Analiza procesu wykrawania Strefa I oraz II', style={'textAlign': 'right', 'color': '#b30059'},
                 href='/page-2'),
        style={"marginRight": 100, 'textAlign': 'right'}),
    html.Div(
        html.A("Powrót do CODESYS", href='http://192.168.1.2:8080/webvisu.htm', target="_blank",
               style={'textAlign': 'right', 'color': '#b30059'}),
        style={"marginRight": 100, 'textAlign': 'right'}
    )

])
