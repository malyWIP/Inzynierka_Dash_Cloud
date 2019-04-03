import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import csv
import os #os module imported here
import flask
# from function_add.watchfolder import watch_dog

# from app_tester import move_to_directory
from class_add.DataProcessing import DataMove


# import pandas as pd
html.Div(id='run-log-storage', style={'display': 'none'}),

path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\testowy\\'
freq = 0.5



# def get_logo():
#     image = "images/dash-logo-stripe.png"
#     encoded_image = base64.b64encode(open(image, "rb").read())
#     logo = html.Div(
#         html.Img(
#             src="data:image/png;base64,{}".format(encoded_image.decode()), height="57"
#         ),
#         style={"marginTop": "0"},
#         className="sept columns",
#     )
#     return logo

def force_motion_value(plots):
    line_count = 0
    x = []
    y = []

    for row in plots:
        if line_count < 280:
            line_count += 1
        else:
            if line_count <400:
                x.append(float(row[1]))
                y.append(float(row[2]))
                line_count += 1
    return x, y


# def motion_value(plots):
#     line_count = 0
#     y = []
#     for row in plots:
#         if line_count < 280:
#             line_count += 1
#         else:
#             y.append(float(row[2]))
#             line_count += 1
#     return y


# def force_value(plots):
#     line_count = 0
#     y = []
#     for row in plots:
#         if line_count < 280:
#             line_count += 1
#         else:
#             y.append(float(row[1]))
#             line_count += 1
#     return y


def get_latest(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    if not files:
        return None
    else:
        return files[0]


def file_to_analizes():
    time_sorted_list = None
    try:
        folder_path = r'D:\STUDIA\Inżynierka\testowy'
        time_sorted_list = get_latest(folder_path)

        # except FileNotFoundError:
        #     print('bład')
    except IndexError:
        print('blad')
    if time_sorted_list is None:
        plots = None
    else:
        csv_file = open(time_sorted_list)
        plots = csv.reader(csv_file, delimiter=';')
    return plots

# def plot_refresh(folder_path):
#
#     if watch_dog(folder_path) == True:
#         return False
#     else:
#         return True

server = flask.Flask(__name__)
app = dash.Dash(__name__,server=server)
server=app.server
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

# @app.callback(
#     Output('result', 'children'),
#     event= [Event('interval-component', 'interval')]
#     [Input('input-x', 'value')]
# )
# def update_result(x):
#     y=update_graph_scatter
#     return "The sum is: {}".format(y)


@app.callback(Output('interval-log-update', 'interval'),
              [Input('dropdown-interval-control', 'value')])
def update_interval_log_update(interval_rate):
    if interval_rate == 'fast':
        return 100

    elif interval_rate == 'regular':
        return 1000

    elif interval_rate == 'slow':
        return 5 * 1000

    # Refreshes every 24 hours
    elif interval_rate == 'no':
        return 24 * 60 * 60 * 1000


# @app.callback(Output('result', 'children'),
#               [Input('interval-log-update', 'n_intervals')])
# def update_div_current_accuracy_value(file_to_analizing):
#
#             y = get_latest(r'D:\STUDIA\Inżynierka\testowy')
#             return [
#                 html.P(
#                     "Analizowany Plik",
#                     style={
#                         'font-weight': 'bold',
#                         'margin-top': '15px',
#                         'margin-bottom': '0px'
#                     }
#                 ),
#                 html.Div(y),
#             ]

# @app.callback(Output('container', 'children'),
#               [Input('Start', 'n_clicks_timestamp'),
#                Input('Stop', 'n_clicks_timestamp')])
# def display(btn1, btn2):
#     if int(btn1) > int(btn2):
#         zebra.setState(True)
#         zebra.move_to_directory(path, moveto, freq)
#
#         msg = 'Button 1 was most recently clicked'
#
#     elif int(btn2) > int(btn1):
#         msg = 'Button 2 was most recently clicked'
#         zebra.setState(False)
#
#     else:
#         zebra.setState(False)
#         x = 0
#         msg = 'None of the buttons have been clicked yet'


# @app.callback(Output('watchdog', 'children'))
# def update_div_current_accuracy_value(file_to_analizing):
#
#             y = plot_refresh(r'D:\STUDIA\Inżynierka\testowy')
#             print(y)
#             return y
            #     html.P(
            #         "Current Accuracy:",
            #         style={
            #             'font-weight': 'bold',
            #             'margin-top': '15px',
            #             'margin-bottom': '0px'
            #         }
            #     ),
            #     html.Div(y),
            # ]


@app.callback(Output('live-update-graph-scatter', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    line_count = 0
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = force_motion_value(plots)
        # x = force_value(plots)
        # y = motion_value(plots)
        # print(y)
        # y = motion_value(plots)
        # print(x)
        # for row in plots:
        #     if line_count < 280:
        #         line_count += 1
        #     else:
        #         x.append(float(row[1]))
        #         y.append(float(row[2]))
        #         line_count += 1
        traces.append(plotly.graph_objs.Scatter(
            x=x[0],
            y=x[1],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        # print(traces)
        return {'data': traces}
    elif not plots:
        traces.append(plotly.graph_objs.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces}
    # elif plots is None:
    #     traces.append(plotly.graph_objs.Scatter(
    #     x=[],
    #     y=[],
    #     name='Scatter {}'.format(1),
    #     mode='lines+markers'))
    #     return {'data': traces}

# @app.callback(Output('live-update-graph-bar', 'figure'),
#               events=[Event('interval-component', 'interval')])
# def update_graph_bar():
#
#     traces = list()
#     for t in range(2):
#         traces.append(plotly.graph_objs.Bar(
#             x=[1, 2, 3, 4, 5],
#             y=[(t + 1) * random() for i in range(5)],
#             name='Bar {}'.format(t)
#             ))
#     layout = plotly.graph_objs.Layout(
#     barmode='group'
# )
#     return {'data': traces, 'layout': layout}

#
# if __name__ == '__main__':
#     # zebra = DataMove(True)
#     app.run_server(host = '0.0.0.0',debug=True)
