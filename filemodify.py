import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from app_tester import move_to_directory
import os, shutil, time
path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\testowy\\'
freq = 2

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn-1', n_clicks_timestamp='0'),
    html.Button('Button 2', id='btn-2', n_clicks_timestamp='0'),
    html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              [Input('btn-1', 'n_clicks_timestamp'),
               Input('btn-2', 'n_clicks_timestamp')])
def display(btn1, btn2):
    if int(btn1) > int(btn2):
        x = 1
        msg = 'Button 1 was most recently clicked'
    elif int(btn2) > int(btn1):
        msg = 'Button 2 was most recently clicked'
        x = 0
    else:
        x = 0
        msg = 'None of the buttons have been clicked yet'

    move_to_directory(path, moveto, freq, x)

    # return html.Div([
    #     html.Div('btn1: {}'.format(x)),
    #     html.Div('btn2: {}'.format(x)),
    #     html.Div(msg)
    # ])




#
# if __name__ == '__main__':
#     app.run_server(debug=True)