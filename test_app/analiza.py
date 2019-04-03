import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import csv
import os #os module imported here
# from function_add.watchfolder import watch_dog

# from app_tester import move_to_directory
from class_add.DataProcessing import DataMove


# import pandas as pd
html.Div(id='run-log-storage', style={'display': 'none'}),

path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\testowy\\'
freq = 0.5
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


def data_separate(plots):
    line_count = 0
    y = []
    for row in plots:
        if line_count < 10:
            line_count += 1
        elif line_count <13: #Data,czas
            y.append((row[1]))
            line_count += 1
        elif line_count == 15: #numer pomiaru
            y.append((row[1]))
            line_count += 1
        elif line_count == 17: #Nazwa
            y.append((row[1]))
            line_count += 1
        elif line_count < 30:
            line_count += 1
        elif line_count < 32: #ostatnia wartosc x,y
            y.append(float(row[1]))
            line_count += 1
        elif line_count == 34: #Peak
            y.append(float(row[1]))
            line_count += 1
        elif line_count == 37:  # Peak
            y.append(float(row[4]))
            line_count += 1
        elif line_count < 223:
            line_count += 1
        elif line_count < 225: #Granice pomiaru w dlugosci
            y.append((row[2]))
            line_count += 1
        elif line_count < 270:
            line_count += 1
        elif line_count == 270:  #Liczba pomiarow
            y.append((row[1]))
            line_count += 1
        else:
            line_count += 1
    return y


def Pomiar_sil(plots):
    max_force = float(data_separate(file_to_analizes())[8])
    max_force1=max_force*0.99
    dzielnik = max_force1/100
    line_count = 0
    row_count = 0
    stage1=0
    stage2=0
    z=0
    y = []
    x = []
    x1 = []
    y1 = []
    peak = 0
    for row in plots:
        if line_count <= 280:
            line_count += 1
            row_count += 1
        elif line_count > 280 and row != 'Sequence Editor' and peak != 1:
                if z < max_force1:
                    z = round(float(row[2]),4)
                    y.append(z)
                    x.append(float(row[1]))
                    line_count += 1
                    row_count += 1
                    stage1 += 1
                    # x.append(float(stage1))
                else:
                    peak=1
        elif row.__len__() > 2 and row[3] != '' and peak == 1 :
            g = round(float(row[2]), 4)
            y1.append(g)
            x1.append(float(row[1]))
            line_count += 1
            row_count += 1
            stage2 += 1
            # x1.append(float(stage2))
    return x,y,x1,y1,dzielnik


def Delta_Force_Stage_1():
    strefa_1 = []
    strefa_2 = []
    strefa_11 = []
    strefa_22 = []
    stage1=0
    stage2=0
    change = 0
    przedzial = Pomiar_sil(file_to_analizes())[1]
    dzielnik = Pomiar_sil(file_to_analizes())[4]
    try:
        for w in range(len(przedzial)):
            if float(w) > 0:
                z = float(przedzial[w] - przedzial[w-1])
                round(z,4)
                if z < dzielnik and change != 1:
                    strefa_1.append(float(round(z,4)))
                    stage1 += 1
                    strefa_11.append(float(stage1))
                elif z >= dzielnik and change !=1:
                    change = 1
                elif change == 1:
                    strefa_2.append(float(round(z,4)))
                    stage2 += 1
                    strefa_22.append(float(stage2))
        return strefa_1,strefa_11,strefa_2,strefa_22
    except IndexError:
        print('brak do przeliczenia liczb')
        return strefa_1,strefa_11,strefa_2,strefa_22

def Delta_Force_Stage_2(delta_force):
    strefa_3 = []
    strefa_4 = []
    strefa_33 = []
    strefa_44 = []
    change = 0
    stage3 = 0
    stage4 = 0
    przedzial = Pomiar_sil(file_to_analizes())[1]
    try:
        for w in range(len(delta_force)):
            z = float(delta_force[w+1] - delta_force[w])
            round(z,2)
            if z < 0 and change != 1:
                strefa_3.append(float(round(z,2)))
            elif z >= 0 and change !=1:
                change = 1
            elif  change == 1:
                strefa_4.append(float(round(z,2)))
        return strefa_3,strefa_4
    except IndexError:
        print('brak do przeliczenia liczb')
        return strefa_3,strefa_4

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
        dcc.Graph(id='live-update-graph-scatter1', animate=False),
        dcc.Graph(id='live-update-graph-scatter2', animate=False),
        dcc.Graph(id='live-update-graph-scatter3', animate=False),
        # dcc.Graph(id='live-update-graph-bar'),

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


@app.callback(Output('live-update-graph-scatter', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Pomiar_sil(plots)
        traces.append(plotly.graph_objs.Scatter(
            x=x[0],
            y=x[1],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces}
    elif not plots:
        traces.append(plotly.graph_objs.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces}
@app.callback(Output('live-update-graph-scatter1', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter1(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Pomiar_sil(plots)
        traces.append(plotly.graph_objs.Scatter(
            x=x[2],
            y=x[3],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces}
    elif not plots:
        traces.append(plotly.graph_objs.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces}

@app.callback(Output('live-update-graph-scatter2', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter1(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Delta_Force_Stage_1()
        traces.append(plotly.graph_objs.Scatter(
            x=x[1],
            y=x[0],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces}
    elif not plots:
        traces.append(plotly.graph_objs.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces}
@app.callback(Output('live-update-graph-scatter3', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter1(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Delta_Force_Stage_1()
        traces.append(plotly.graph_objs.Scatter(
            x=x[3],
            y=x[2],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces}
    elif not plots:
        traces.append(plotly.graph_objs.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces}

if __name__ == '__main__':
    app.run_server(debug=True)
