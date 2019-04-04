# In[]:
# Import required libraries
import dash
import dash_html_components as html
from dash.dependencies import Input, Output


# Define the app
app = dash.Dash('')
server = app.server
app.config.suppress_callback_exceptions = False
app.scripts.config.serve_locally = True


class DashCallbackVariables:
    """Class to store information useful to callbacks"""

    def __init__(self):
        self.n_clicks = {1: 0, 2: 0}

    def update_n_clicks(self, nclicks, bt_num):
        self.n_clicks[bt_num] = nclicks


callbacks_vars = DashCallbackVariables()

root_layout = html.Div(
    id='main_page',
    children=[
        html.Div(
                id='btn_name',
                children="No button was clicked"
        ),
        html.Div(
            [
                html.Button(
                    'Button1',
                    id='btn_1',
                    type='submit'
                )
            ]
        ),
        html.Div(
            [
                html.Button(
                    'Button2',
                    id='btn_2',
                    type='submit'
                )
            ]
        )
    ]
)

app.layout = root_layout


@app.callback(
    Output('btn_name', 'children'),
    [
        Input('btn_1', 'n_clicks'),
        Input('btn_2', 'n_clicks'),
    ]
)
def btn_click_callback(nclick_bt1, nclick_bt2):

    # If you have more than one Input, then you need to add this
    # otherwise before the button is clicked its value by default is None
    if nclick_bt1 is None:
        nclick_bt1 = 0
    if nclick_bt2 is None:
        nclick_bt2 = 0

    answer = "No button was clicked"

    if nclick_bt1 != callbacks_vars.n_clicks[1]:
        # It was triggered by a click on the button 1
        callbacks_vars.update_n_clicks(nclick_bt1, 1)

        answer = "Button 1 was clicked"

    if int(nclick_bt2) != callbacks_vars.n_clicks[2]:
        # It was triggered by a click on the button 2
        callbacks_vars.update_n_clicks(nclick_bt2, 2)

        answer = "Button 2 was clicked"

    return answer


# In[]:
# Main
# if __name__ == '__main__':
#     app.run_server(debug=True)