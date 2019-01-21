
from class_add.DataProcessing import DataMove
from dash_web.Controller_Interaction import*

global zebra

zebra = DataMove(True)


if __name__ == '__main__':
    app.run_server(debug=True)