

from dash_web.Model_Manipulation import*
from dash_web.View_Layout import*
from appMain import process_tester
from appMain import reset_data
from appMain import callbacks_vars
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc


#############################################
# Interaction Between Components / Controller
#############################################

#ZMIENNE
# path = r'D:\STUDIA\Inżynierka\test\\'
# moveto = r'D:\STUDIA\Inżynierka\Dash_App\csv_memory\\'
freq = 1

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
    elif pathname == '/page-3':
        return page_3_layout
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
        return 1000

    elif interval_rate == 'regular':
        return 5000

    elif interval_rate == 'slow':
        return 10 * 1000

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
    if btn1 is None:
        btn1=0
    if btn2 is None:
        btn2 = 0
    if btn3 is None:
        btn3 = 0

        msg = 'Button 1 was most recently clicked'
    if btn1 != callbacks_vars.n_clicks[1]:
        # It was triggered by a click on the button 1
        callbacks_vars.update_n_clicks(btn1, 1)
        process_tester.setState(True)
        reset_data.setState(False)
        process_tester.move_to_directory(path, moveto, freq)

    elif btn2 != callbacks_vars.n_clicks[2]:
        # It was triggered by a click on the button 1
        callbacks_vars.update_n_clicks(btn2, 2)
        reset_data.setState(False)
        process_tester.setState(False)
    elif btn3 != callbacks_vars.n_clicks[3]:
        # It was triggered by a click on the button 1
        callbacks_vars.update_n_clicks(btn3, 3)
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
            stan1=Analiza_Stref_I()[0]
            kolor1 = Analiza_Stref_I()[1]
            stan2 = Analiza_Stref_II()[0]
            kolor2 = Analiza_Stref_II()[1]
            stan3 = Analiza_Stref_III()[0]
            kolor3 = Analiza_Stref_III()[1]
            stan4 = Analiza_Stref_IV()[0]
            kolor4 = Analiza_Stref_IV()[1]

            return [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div('Strefa I'), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue',
                                    'borderRadius': '5px',
                                    'font-weight': 'bold'}),
                                dbc.Col(html.Div("Strefa II"), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue ',
                                    'borderRadius': '5px',
                                    'font-weight': 'bold',}),
                                dbc.Col(html.Div("Strefa III"), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue ',
                                    'borderRadius': '5px',
                                    'font-weight': 'bold',}),
                                dbc.Col(html.Div("Strefa IV"), width=1, style={
                                    'backgroundColor': 'DeepSkyBlue ',
                                    'borderRadius': '5px',
                                    'font-weight': 'bold',}),
                            ],justify="center",style={'textAlign':'center'}),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(stan1), width=1, style={
                                    'backgroundColor': kolor1,
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div(stan2), width=1, style={
                                    'backgroundColor': kolor2,
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div(stan3), width=1, style={
                                    'backgroundColor': kolor3,
                                    'borderRadius': '5px'}),
                                dbc.Col(html.Div(stan4), width=1, style={
                                    'backgroundColor': kolor4,
                                    'borderRadius': '5px'}),
                            ],justify="center",style={'textAlign':'center'})
                    ])]
    except TypeError:
        print('bład')


@app.callback(Output('edge-sharpness-final', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def Stan_Ostrza(elo):
    try:
        if get_latest(moveto) is not None:
            stan = Stan_Koncowy_Ostrza()[0]
            kolor = Stan_Koncowy_Ostrza()[1]

            return [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div('Stan Ostrza'), width=2, style={
                                    'backgroundColor': 'DeepSkyBlue',
                                    'borderRadius': '5px',
                                    'font-weight': 'bold',
                                    'size': 30}),
                            ], justify="center", style={'textAlign': 'center'}),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(stan), width=2, style={
                                    'backgroundColor': kolor,
                                    'borderRadius': '5px'}),
                            ], justify="center", style={'textAlign': 'center'})
                    ],style={'size': 200})]
    except TypeError:
        print('bład')


@app.callback(Output('live-update-graph-scatter', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    # a = test.get_latest(moveto)
    # b=test.file_to_analizes(moveto,a)
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
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa I i II')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
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

@app.callback(Output('live-update-graph-scatter4', 'figure'),
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
            x=x[2],
            y=x[3],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa III i IV')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa III i IV')}


@app.callback(Output('live-update-graph-scatter5', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Delta_Force_Stage_2()
        traces.append(go.Scatter(
            x=x[1],
            y=x[0],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa III - oderwanie materiału od blachy')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa III oderwanie materiału od blachy')}


@app.callback(Output('live-update-graph-scatter6', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    plots = file_to_analizes()
    traces = list()
    traces.clear()
    if plots is not None:
        x = Delta_Force_Stage_2()
        traces.append(go.Scatter(
            x=x[3],
            y=x[2],
            name='Scatter {}'.format(1),
            mode='lines+markers'
            ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa IV - wyjście ostrza z materiału')}
    elif not plots:
        traces.append(go.Scatter(
            x=x,
            y=y,
            name='Scatter {}'.format(1),
            mode='lines+markers'
        ))
        return {'data': traces,
                'layout': go.Layout(xaxis={'title': 'nr pomiaru'}, yaxis={'title': 'Siła [N]'},
                                    title='Strefa IV - wyjście ostrza z materiału')}