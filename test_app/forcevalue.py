import csv
import os #os module imported here
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
    row_count = 0
    x = []
    y = []

    for row in plots:

        if line_count <= 280:
            line_count += 1
            row_count +=1
        elif line_count > 280 and row != 'Sequence Editor':

                y.append(float(row[2]))
                line_count += 1
                row_count += 1
    return x, y

def Pomiar_sil(plots):
    max_force = float(data_separate(file_to_analizes())[8])
    print(max_force)
    line_count = 0
    row_count = 0
    y = []
    peak = 0
    for row in plots:
        if line_count <= 280:
            line_count += 1
            row_count += 1
        elif line_count > 280 and row != 'Sequence Editor' and peak != 1:
                peak = y.count(max_force)
                z = round(float(row[2]),2)
                y.append(z)
                line_count += 1
                row_count += 1
        else:
            line_count += 1
    return  y

def Delta_Force(delta_force):
    strefa_1 = []
    strefa_2 = []
    change = 0
    try:
        for w in range(len(delta_force)):
            z = float(delta_force[w+1] - delta_force[w])
            round(z,2)
            if z < 50 and change != 1:
                strefa_1.append(float(round(z,4)))
            else:
                change = 1
                strefa_2.append(float(round(z,4)))
        return strefa_1,strefa_2
    except IndexError:
        print('brak do przeliczenia liczb')
        return strefa_1,strefa_2


def Przeliczena_elo():
    x  = [1,2,3,4,5,6]
    y = [1,2,3,4,5,6]
    for w in range(0,len(x)):
        z= y[w] - x[w]
        print(z)

def data_separate(plots):
    line_count = 0
    y = []
    for row in plots:
        if line_count < 10:
            line_count += 1
        elif line_count <13: #Data,czas
            y.append((row[1]))
            line_count += 1
        elif line_count == 15: #numer pomiaru
            y.append((row[1]))
            line_count += 1
        elif line_count == 17: #Nazwa
            y.append((row[1]))
            line_count += 1
        elif line_count < 30:
            line_count += 1
        elif line_count < 32: #ostatnia wartosc x,y
            y.append(float(row[1]))
            line_count += 1
        elif line_count == 34: #Peak
            y.append(float(row[1]))
            line_count += 1
        elif line_count == 37:  # Peak
            y.append(float(row[4]))
            line_count += 1
        elif line_count < 223:
            line_count += 1
        elif line_count < 225: #Granice pomiaru w dlugosci
            y.append((row[2]))
            line_count += 1
        elif line_count < 270:
            line_count += 1
        elif line_count == 270:  #Liczba pomiarow
            y.append((row[1]))
            line_count += 1
        # elif line_count < 34:
        #     line_count += 1
        # elif line_count == 35:
        #     y.append(float(row[1]))
        #     line_count += 1
        else:
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

        # print(data_separate(file_to_analizes()))
        # print(motion_value(file_to_analizes()))
        # print(force_value(file_to_analizes()))
        # print(Pomiar_sil(file_to_analizes()))
        print(Delta_Force(Pomiar_sil(file_to_analizes())))
        time.sleep(10)
