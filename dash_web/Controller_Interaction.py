

from dash_web.Model_Manipulation import*
from dash_web.View_Layout import*
from app import process_tester
from app import reset_data
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

#############################################
# Interaction Between Components / Controller
#############################################

#ZMIENNE
# path = r'D:\STUDIA\Inżynierka\test\\'
# moveto = r'D:\STUDIA\Inżynierka\Dash_App\csv_memory\\'
freq = 0.1

html.Div(id='run-log-storage', style={'display': 'none'}),


@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page


@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


@app.callback(Output('interval-log-update', 'interval'),
              [Input('dropdown-interval-control', 'value')])
def update_interval_log_update(interval_rate):
    if interval_rate == 'fast':
        return 200

    elif interval_rate == 'regular':
        return 1000

    elif interval_rate == 'slow':
        return 5 * 1000

    # Refreshes every 24 hours
    elif interval_rate == 'no':
        return 24 * 60 * 60 * 1000


# @app.callback(Output('result', 'children'),
#               [Input('interval-log-update', 'n_intervals')])
# def update_current_file_analizes(file_to_analizing):
#
#             y = get_latest(moveto)
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


@app.callback(Output('container', 'children'),
              [Input('Start', 'n_clicks'),
               Input('Stop', 'n_clicks'),
               Input('Reset', 'n_clicks')])
def start_stop_button(btn1, btn2, btn3):
    if int(btn1) > int(btn2) and int(btn1) > int(btn3):
        process_tester.setState(True)
        reset_data.setState(False)
        process_tester.move_to_directory(path, moveto, freq)
        msg = 'Button 1 was most recently clicked'

    elif int(btn2) > int(btn1) and int(btn2) > int(btn3):
        msg = 'Button 2 was most recently clicked'
        reset_data.setState(False)
        process_tester.setState(False)
    elif int(btn3) > int(btn1) and int(btn3) > int(btn2):
        msg = 'Button 2 was most recently clicked'
        reset_data.setState(True)
        process_tester.setState(False)
        reset_data.move_to_directory(moveto,path)
    else:
        reset_data.setState(False)
        process_tester.setState(False)
        x = 0
        msg = 'None of the buttons have been clicked yet'


@app.callback(Output('Process_Parameters', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def update_edge_sharpness(file_to_analizing):
    try:
        if get_latest(moveto) is not None:
            data = data_separate(file_to_analizes())[0]
            czas = data_separate(file_to_analizes())[1]
            num_cyklu = float(data_separate(file_to_analizes())[2])
            nazwa = data_separate(file_to_analizes())[3]
            max_sil = data_separate(file_to_analizes())[8]
            min_x = data_separate(file_to_analizes())[9]
            max_x = data_separate(file_to_analizes())[10]
            point_nr = data_separate(file_to_analizes())[11]
            return [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div("Data"), width=1, style={'borderWidth': '1px',
                                                                          'font-weight': 'bold',
                                                                          'textAlign': 'center',
                                                                          'borderStyle': 'solid',
                                                                          'borderColor': '#000066',
                                                                          'backgroundColor': 'DeepSkyBlue ',
                                                                          'borderRadius': '5px'}),
                                dbc.Col(html.Div("Godzina"), width=1, style={'borderWidth': '1px',
                                                                             'font-weight': 'bold',
                                                                             'textAlign': 'center',
                                                                             'borderStyle': 'solid',
                                                                             'borderColor': '#000066',
                                                                             'backgroundColor': 'DeepSkyBlue ',
                                                                             'borderRadius': '5px'}),
                                dbc.Col(html.Div("Numer Cyklu"), width=1, style={'borderWidth': '1px',
                                                                                 'font-weight': 'bold',
                                                                                 'textAlign': 'center',
                                                                                 'borderStyle': 'solid',
                                                                                 'borderColor': '#000066',
                                                                                 'backgroundColor': 'DeepSkyBlue ',
                                                                                 'borderRadius': '5px'}),
                                dbc.Col(html.Div("Nazwa Pliku"), width=2, style={'borderWidth': '1px',
                                                                                 'font-weight': 'bold',
                                                                                 'textAlign': 'center',
                                                                                 'borderStyle': 'solid',
                                                                                 'borderColor': '#000066',
                                                                                 'backgroundColor': 'DeepSkyBlue ',
                                                                                 'borderRadius': '5px'}),
                                dbc.Col(html.Div("Max Siła Wykrawania [N]"), width=2, style={'borderWidth': '1px',
                                                                                             'font-weight': 'bold',
                                                                                             'textAlign': 'center',
                                                                                             'borderStyle': 'solid',
                                                                                             'borderColor': '#000066',
                                                                                             'backgroundColor': 'DeepSkyBlue ',
                                                                                             'borderRadius': '5px'}),
                                dbc.Col(html.Div("Min wychylenie [mm]"), width=2, style={'borderWidth': '1px',
                                                                                         'font-weight': 'bold',
                                                                                         'textAlign': 'center',
                                                                                         'borderStyle': 'solid',
                                                                                         'borderColor': '#000066',
                                                                                         'backgroundColor': 'DeepSkyBlue ',
                                                                                         'borderRadius': '5px'}),
                                dbc.Col(html.Div("Max wychylenie [mm]"), width=2, style={'borderWidth': '1px',
                                                                                         'font-weight': 'bold',
                                                                                         'textAlign': 'center',
                                                                                         'borderStyle': 'solid',
                                                                                         'borderColor': '#000066',
                                                                                         'backgroundColor': 'DeepSkyBlue ',
                                                                                         'borderRadius': '5px'}),
                                dbc.Col(html.Div("Ilość pkt. pomiar."), width=1, style={'borderWidth': '1px',
                                                                                        'font-weight': 'bold',
                                                                                        'textAlign': 'center',
                                                                                        'borderStyle': 'solid',
                                                                                        'borderColor': '#000066',
                                                                                        'backgroundColor': 'DeepSkyBlue ',
                                                                                        'borderRadius': '5px'}),
                            ]),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(data), width=1, style={'borderWidth': '1px',
                                                                        'textAlign': 'center',
                                                                        'borderStyle': 'solid',
                                                                        'borderColor': '#b3d9ff',
                                                                        'backgroundColor': 'DeepSkyBlue ',
                                                                        'borderRadius': '5px'}),
                                dbc.Col(html.Div(czas), width=1, style={'borderWidth': '1px',
                                                                        'textAlign': 'center',
                                                                        'borderStyle': 'solid',
                                                                        'borderColor': '#b3d9ff',
                                                                        'backgroundColor': 'DeepSkyBlue ',
                                                                        'borderRadius': '5px'}),
                                dbc.Col(html.Div(num_cyklu), width=1, style={'borderWidth': '1px',
                                                                             'textAlign': 'center',
                                                                             'borderStyle': 'solid',
                                                                             'borderColor': '#b3d9ff',
                                                                             'backgroundColor': 'DeepSkyBlue ',
                                                                             'borderRadius': '5px'}),
                                dbc.Col(html.Div(nazwa), width=2, style={'borderWidth': '1px',
                                                                         'textAlign': 'center',
                                                                         'borderStyle': 'solid',
                                                                         'borderColor': '#80b3ff',
                                                                         'w3Panel': 'w3Green',
                                                                         'backgroundColor': 'DeepSkyBlue ',
                                                                         'borderRadius': '5px'}),
                                dbc.Col(html.Div(max_sil), width=2, style={'borderWidth': '1px',
                                                                           'textAlign': 'center',
                                                                           'borderStyle': 'solid',
                                                                           'borderColor': '#80b3ff',
                                                                           'w3Panel': 'w3Green',
                                                                           'backgroundColor': 'DeepSkyBlue ',
                                                                           'borderRadius': '5px'}),
                                dbc.Col(html.Div(min_x), width=2, style={'borderWidth': '1px',
                                                                         'textAlign': 'center',
                                                                         'borderStyle': 'solid',
                                                                         'borderColor': '#80b3ff',
                                                                         'w3Panel': 'w3Green',
                                                                         'backgroundColor': 'DeepSkyBlue ',
                                                                         'borderRadius': '5px'}),
                                dbc.Col(html.Div(max_x), width=2, style={'borderWidth': '1px',
                                                                         'textAlign': 'center',
                                                                         'borderStyle': 'solid',
                                                                         'borderColor': '#80b3ff',
                                                                         'w3Panel': 'w3Green',
                                                                         'backgroundColor': 'DeepSkyBlue ',
                                                                         'borderRadius': '5px'}),
                                dbc.Col(html.Div(point_nr), width=1, style={'borderWidth': '1px',
                                                                            'textAlign': 'center',
                                                                            'borderStyle': 'solid',
                                                                            'borderColor': '#80b3ff',
                                                                            'w3Panel': 'w3Green',
                                                                            'backgroundColor': 'DeepSkyBlue ',
                                                                            'borderRadius': '5px'}),

                            ]),
                    ]),
            ]
    except TypeError:
        print('brak plików')

@app.callback(Output('edge-sharpness', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def Stan_Ostrza(elo):
    try:
        if get_latest(moveto) is not None:
            stan=Analiza_Stref()[0]
            kolor = Analiza_Stref()[1]
            return [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div('Strefa I'), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue',
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div("Strefa II"), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue ',
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div("Strefa III"), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue ',
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div("Strefa IV"), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue ',
                                    'borderRadius': '5px'}),
                            ],justify="center",style={'textAlign':'center'}),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(stan), width=1, style={
                                    'backgroundColor': kolor,
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div(stan), width=1, style={
                                    'backgroundColor': kolor,
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div(stan), width=1, style={
                                    'backgroundColor': kolor,
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div(stan), width=1, style={
                                    'backgroundColor': kolor,
                                    'borderRadius': '5px'}),
                            ],justify="center",style={'textAlign':'center'})
                    ])]
    except TypeError:
        print('bład')


@app.callback(Output('live-update-graph-scatter', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = force_motion_value(plots)
        traces.append(go.Scatter(
            x=x[0],
            y=x[1],
            name='Scatter {}'.format(1),
            mode='lines+markers',

            ))

        # print(traces)
        return {'data': traces, 'layout': go.Layout(xaxis={'title': 'Przemieszczenie [mm]'}, yaxis={'title': 'Siła [N]'},title='Charakterystyka Procesu Wykrawania')}

    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))

        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'Przemieszczenie [mm]'}, yaxis={'title': 'Siła [N]'}, title='Charakterystyka Procesu Wykrawania')}


@app.callback(Output('live-update-graph-scatter1', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Pomiar_sil(plots)
        traces.append(go.Scatter(
            x=x[0],
            y=x[1],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'Przemieszczenie [mm]'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa I i II')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'Przemieszczenie [mm]'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa I i II')}


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
        traces.append(go.Scatter(
            x=x[1],
            y=x[0],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr Pomiaru'}, yaxis={'title': 'Różnica Siły [N]'},
                                    title='Strefa I - Pierwszy kontakt Ostrza z materiałem')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr Pomiaru'}, yaxis={'title': 'Różnica Siły [N]'},
                                    title='Strefa I - Pierwszy kontakt Ostrza z materiałem')}


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
        traces.append(go.Scatter(
            x=x[3],
            y=x[2],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr Pomiaru'}, yaxis={'title': 'Różnica Siły [N]'},
                                    title='Strefa  II - Proces Wykrawania, ostrze zagłebia sie w materiał')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr Pomiaru'}, yaxis={'title': 'Różnica Siły [N]'},
                                    title='Strefa  II - Proces Wykrawania, ostrze zagłebia sie w materiał')}