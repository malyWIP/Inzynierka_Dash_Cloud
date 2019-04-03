# !/usr/bin/env python

from class_add.DataProcessing import DataMove
from dash_web.Controller_Interaction import*
from class_add.DataDelete import DataDel


process_tester = DataMove(True)
reset_data = DataDel(True)

# if __name__ == '__main__':
#     app.run_server(host='0.0.0.0',debug=True)
