# !/usr/bin/env python

from class_add.DataProcessing import DataMove
from dash_web.Controller_Interaction import*
from class_add.DataDelete import DataDel
from class_add.ButtonDef import DashCallbackVariables
from class_add.listener import Watcher
# from class_add.listener import Watcher
# from Rpi_functions.Gpio_Activities import Przezbrojenie

callbacks_vars = DashCallbackVariables()
process_tester = DataMove(True)
reset_data = DataDel(True)
licznik = Watcher(File_Change1())
# w = Watcher()
if __name__ == '__main__':
    # w.run()
    app.run_server(host='0.0.0.0',debug=True)
    # Przezbrojenie()
