

from dash_web.Model_Manipulation import*
from dash_web.View_Layout import*
from main.app import zebra
from dash.dependencies import Output, Event, Input
import plotly


#############################################
# Interaction Between Components / Controller
#############################################

html.Div(id='run-log-storage', style={'display': 'none'}),

path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\testowy\\'
freq = 0.5


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
def update_div_current_accuracy_value(file_to_analizing):

            y = get_latest(r'D:\STUDIA\Inżynierka\testowy')
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
def display(btn1, btn2):
    if int(btn1) > int(btn2):
        zebra.setState(True)
        zebra.move_to_directory(path, moveto, freq)

        msg = 'Button 1 was most recently clicked'

    elif int(btn2) > int(btn1):
        msg = 'Button 2 was most recently clicked'
        zebra.setState(False)

    else:
        zebra.setState(False)
        x = 0
        msg = 'None of the buttons have been clicked yet'


@app.callback(Output('watchdog', 'children'))
def update_div_current_accuracy_value(file_to_analizing):

            y = plot_refresh(r'D:\STUDIA\Inżynierka\testowy')
            print(y)
            return y
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
              events=[Event('interval-component', 'interval')])
def update_graph_scatter():
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


# if __name__ == '__main__':
#     zebra = kupa(True)
#     app.run_server(debug=True)