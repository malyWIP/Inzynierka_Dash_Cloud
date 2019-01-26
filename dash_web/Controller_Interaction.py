

from dash_web.Model_Manipulation import*
from dash_web.View_Layout import*
from app import process_tester
from dash.dependencies import Output, Event, Input
import plotly


#############################################
# Interaction Between Components / Controller
#############################################

#ZMIENNE
path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\Dash_App\csv_memory\\'
freq = 0.5

html.Div(id='run-log-storage', style={'display': 'none'}),


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
              [Input('Start', 'n_clicks_timestamp'),
               Input('Stop', 'n_clicks_timestamp')])
def start_stop_button(btn1, btn2):
    if int(btn1) > int(btn2):
        process_tester.setState(True)
        process_tester.move_to_directory(path, moveto, freq)

        msg = 'Button 1 was most recently clicked'

    elif int(btn2) > int(btn1):
        msg = 'Button 2 was most recently clicked'
        process_tester.setState(False)

    else:
        process_tester.setState(False)
        x = 0
        msg = 'None of the buttons have been clicked yet'


@app.callback(Output('edge-sharpness', 'children'),
              [Input('interval-log-update', 'n_intervals')])
def update_edge_sharpness(file_to_analizing):
    x = edge_sharpness_result(force_motion_value(file_to_analizes(moveto))[1])
    if x > 2000:
        z = 'tępe'
    else:
        z = 'ostre'
    return [
        html.P(
            "Current Accuracy:",
            style={
                'font-weight': 'bold',
                'margin-top': '15px',
                'margin-bottom': '0px'
            }
        ),
        html.Div(z),html.Div(x)
    ]


@app.callback(Output('live-update-graph-scatter', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_scatter():
    x = []
    y = []
    plots = file_to_analizes(moveto)
    traces = list()
    traces.clear()
    if plots is not None:
        x = force_motion_value(plots)
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


# if __name__ == '__main__':
#     zebra = kupa(True)
#     app.run_server(debug=True)