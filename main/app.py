
from class_add.DataProcessing import DataMove
from dash_web.Controller_Interaction import*

global process_tester

process_tester = DataMove(True)


if __name__ == '__main__':
    app.run_server(debug=True)
