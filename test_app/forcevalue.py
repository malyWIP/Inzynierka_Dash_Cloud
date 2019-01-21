import csv
import os #os module imported here
# from app_tester import move_to_directory
import time

def get_latest(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    if not files:
        return None
    else:
        return files[0]


def file_to_analizes():
    time_sorted_list = None
    try:
        folder_path = r'D:\STUDIA\Inżynierka\testowy'
        time_sorted_list = get_latest(folder_path)

        # except FileNotFoundError:
        #     print('bład')
    except IndexError:
        print('blad')
    if time_sorted_list is None:
        plots = None
    else:
        csv_file = open(time_sorted_list)
        plots = csv.reader(csv_file, delimiter=';')
    return plots

def force_motion_value(plots):
    line_count = 0
    x = []
    y = []

    for row in plots:
        if line_count < 280:
            line_count += 1
        else:
            x.append(float(row[1]))
            y.append(float(row[2]))
            line_count += 1
    return x, y


def force_value(plots):
    line_count = 0
    y = []
    for row in plots:
        if line_count < 280:
            line_count += 1
        else:
            y.append(float(row[1]))
            line_count += 1
    return y


def motion_value(plots):
    line_count = 0
    y = []
    for row in plots:
        if line_count < 280:
            line_count += 1
        else:
            y.append(float(row[2]))
            line_count += 1
    return y

if __name__ == '__main__':
    while True:

        # print(force_motion_value(file_to_analizes())[1])
        print(motion_value(file_to_analizes()))
        print(force_value(file_to_analizes()))

        time.sleep(1)
