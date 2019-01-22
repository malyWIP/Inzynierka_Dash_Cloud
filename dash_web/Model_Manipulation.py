
import csv
import os
from function_add.watchfolder import*
import sys

###########################
# Data Manipulation / Model
###########################


def edge_sharpness_result(tab):
    s = sum(tab)
    x = len(tab)
    m = float(s/x)
    return m


def force_motion_value(plots):
    line_count = 0
    x = []
    y = []

    for row in plots:
        if line_count < 280:
            line_count += 1
        elif row.__len__() > 2 and row[3] != '':
            x.append(float(row[1]))
            y.append(float(row[2]))
            line_count += 1
    return x, y


def motion_value(plots):
    line_count = 0
    y = []
    for row in plots:
        if line_count < 280:
            line_count += 1
        else:
            if row[1] != '':
                y.append(float(row[2]))
                line_count += 1
    return y


def force_value(plots):
    line_count = 0
    y = []
    for row in plots:
        if line_count < 280:
            line_count += 1
        else:
            if row[1] != '':
                y.append(float(row[1]))
                line_count += 1
    return y


def get_latest(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    if not files:
        return None
    else:
        return files[0]


def file_to_analizes(folder):
    time_sorted_list = None
    try:
        # folder_path = r'D:\STUDIA\Inżynierka\testowy'
        time_sorted_list = get_latest(folder)

    except IndexError:
        print("IndexError:", sys.exc_info()[0])
    if time_sorted_list is None:
        plots = None
    else:
        csv_file = open(time_sorted_list)
        plots = csv.reader(csv_file, delimiter=';')
    return plots


def plot_refresh(folder_path):
    if watch_dog(folder_path) == True:
        return False
    else:
        return True
