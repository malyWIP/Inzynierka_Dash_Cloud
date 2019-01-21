import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from test_app.app_tester import move_to_directory

path = r'D:\STUDIA\Inżynierka\test\\'
moveto = r'D:\STUDIA\Inżynierka\testowy\\'
freq = 0.5

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Start', id='Start', n_clicks='0'),
    html.Button('Stop', id='Stop', n_clicks='0'),
    html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              [Input('Start', 'n_clicks'),
               Input('Stop', 'n_clicks')])
def display(Start,Stop):

    if int(Start) > int(Stop):
        msg = 'Start'
        x = 1
    else :
        msg = 'Stop'
        x = 0
    move_to_directory(path, moveto, freq, x)
    print(move_to_directory(path, moveto, freq, x))
    return html.Div([html.Div(x)])



# if __name__ == '__main__':
#     app.run_server(debug=True)