

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
path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\Dash_App\csv_memory\\'
freq = 0.5

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
        return 100

    elif interval_rate == 'regular':
        return 1000

    elif interval_rate == 'slow':
        return 5 * 1000

    # Refreshes every 24 hours
    elif interval_rate == 'no':
        return 24 * 60 * 60 * 1000


@app.callback(Output('result', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def update_current_file_analizes(file_to_analizing):

            y = get_latest(moveto)
            return [
                html.P(
                    "Analizowany Plik",
                    style={
                        'font-weight': 'bold',
                        'margin-top': '15px',
                        'margin-bottom': '0px'
                    }
                ),
                html.Div(y),
            ]


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


@app.callback(Output('edge-sharpness', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def update_edge_sharpness(file_to_analizing):
    data = 0
    czas = 0
    num_cyklu=0
    nazwa=0
    nr_pom=0
    max_sil=0
    if get_latest(moveto) is not None:
        data = data_separate(file_to_analizes(moveto))[0]
        czas = data_separate(file_to_analizes(moveto))[1]
        num_cyklu = data_separate(file_to_analizes(moveto))[2]
        nazwa = data_separate(file_to_analizes(moveto))[3]
        nr_pom = data_separate(file_to_analizes(moveto))[4]
        max_sil = data_separate(file_to_analizes(moveto))[7]
    return [
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Div("Data"),width=1,style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'}),
                        dbc.Col(html.Div("Godzina"),width=1, style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'}),
                        dbc.Col(html.Div("Numer Cyklu", style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'})),
                        dbc.Col(html.Div("Nazwa Pliku", style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'})),
                        dbc.Col(html.Div("Numer Pomiaru", style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'})),
                        dbc.Col(html.Div("Max Siła Wykrawania", style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'})),
                        dbc.Col(html.Div("Min przemieszczenie czujnika", style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'})),
                        dbc.Col(html.Div("Max wychylenie czujnika", style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'})),
                    ]),
                dbc.Row(
                    [
                        dbc.Col(html.Div(data),width=1, style={'borderWidth': '1px',
                                                        'borderStyle': 'solid',
                                                        'borderColor': '#80b3ff',
                                                        'w3Panel': 'w3Green',
                                                        'backgroundColor': 'DeepSkyBlue ',
                                                        'borderRadius': '5px'}),
                        dbc.Col(html.Div(czas),width=1, style={'borderWidth': '1px',
                                                           'borderStyle': 'solid',
                                                           'borderColor': '#80b3ff',
                                                           'w3Panel': 'w3Green',
                                                           'backgroundColor': 'DeepSkyBlue ',
                                                           'borderRadius': '5px'}),
                        dbc.Col(html.Div(num_cyklu, style={'borderWidth': '1px',
                                                               'borderStyle': 'solid',
                                                               'borderColor': '#80b3ff',
                                                               'w3Panel': 'w3Green',
                                                               'backgroundColor': 'DeepSkyBlue ',
                                                               'borderRadius': '5px'})),
                        dbc.Col(html.Div(nazwa, style={'borderWidth': '1px',
                                                               'borderStyle': 'solid',
                                                               'borderColor': '#80b3ff',
                                                               'w3Panel': 'w3Green',
                                                               'backgroundColor': 'DeepSkyBlue ',
                                                               'borderRadius': '5px'})),
                        dbc.Col(html.Div(nr_pom, style={'borderWidth': '1px',
                                                                 'borderStyle': 'solid',
                                                                 'borderColor': '#80b3ff',
                                                                 'w3Panel': 'w3Green',
                                                                 'backgroundColor': 'DeepSkyBlue ',
                                                                 'borderRadius': '5px'})),
                        dbc.Col(html.Div(max_sil, style={'borderWidth': '1px',
                                                                                      'borderStyle': 'solid',
                                                                                      'borderColor': '#80b3ff',
                                                                                      'w3Panel': 'w3Green',
                                                                                      'backgroundColor': 'DeepSkyBlue ',
                                                                                      'borderRadius': '5px'})),
                        dbc.Col(html.Div("Min Wychylenie czujnika", style={'borderWidth': '1px',
                                                                           'borderStyle': 'solid',
                                                                           'borderColor': '#80b3ff',
                                                                           'w3Panel': 'w3Green',
                                                                           'backgroundColor': 'DeepSkyBlue ',
                                                                           'borderRadius': '5px'})),
                        dbc.Col(html.Div("Max wychylenie czujnika", style={'borderWidth': '1px',
                                                                           'borderStyle': 'solid',
                                                                           'borderColor': '#80b3ff',
                                                                           'w3Panel': 'w3Green',
                                                                           'backgroundColor': 'DeepSkyBlue ',
                                                                           'borderRadius': '5px'})),
                    ]),
                ]),
            ]
    #     html.Div([
    #         # html.P(
    #         #     "Current Accuracy:",
    #         #     style={
    #         #         'display':'inline-block',
    #         #         'font-weight': 'bold',
    #         #         'margin-top': '15px',
    #         #         'margin-bottom': '0px'
    #         #     }
    #         # ),
    #         html.Div(z, className='six colums',style={
    #                 'display':'inline-block',
    #                 'font-weight': 'bold',
    #                 'margin-top': '15px',
    #                 'margin-bottom': '0px'}),
    #         html.Div(x, className='six colums',style={
    #                 'display':'inline-block',
    #                 'font-weight': 'bold',
    #                 'margin-top': '15px',
    #                 'margin-bottom': '0px'})
    # ],
    # className='row')]


@app.callback(Output('Process_Parameters', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def Process_Parameters(file_to_analizing):
    data=0
    czas=0
    if get_latest(moveto) is not None:
        data = data_separate(file_to_analizes(moveto))[0]
        czas = data_separate(file_to_analizes(moveto))[1]
    return [
        html.P(
            "Current Accuracy:",
            style={
                'font-weight': 'bold',
                'margin-top': '15px',
                'margin-bottom': '0px'
            }
        ),
        html.Div(data),html.Div(czas)
    ]


@app.callback(Output('live-update-graph-scatter', 'figure'),
              [Input('interval-log-update', 'n_intervals')])
def update_graph_scatter(elo):
    x = []
    y = []
    plots = file_to_analizes(moveto)
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
