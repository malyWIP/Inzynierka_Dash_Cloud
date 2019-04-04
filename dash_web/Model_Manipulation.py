
import csv
import os

###########################
# Data Manipulation / Model
###########################

# path = r'D:\STUDIA\Inżynierka\test\\'
# moveto = r'D:\STUDIA\Inżynierka\testowy\\'
path = r'csv_folder\\'
moveto = r'csv_memory\\'

def get_latest(folder):
    try:
        files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        if not files:
            return None
        else:
            return files[0]
    except FileNotFoundError:
        print('nie znaleziono pliku')

def file_to_analizes():
    time_sorted_list = None
    try:
        # folder_path = r'D:\STUDIA\Inżynierka\testowy'
        time_sorted_list = get_latest(moveto)

        if time_sorted_list is None:
            plots = None
        else:
            csv_file = open(time_sorted_list)
            plots = csv.reader(csv_file, delimiter=';')
        return plots
    except IndexError:
        print("IndexError:")
    except FileNotFoundError:
        print("Brak Plików")



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
        else:
            line_count += 1
    return y




def force_motion_value(plots):
    line_count = 0
    x = []
    y = []
    try:
        for row in plots:
            if line_count < 280:
                line_count += 1
            elif row.__len__() > 2 and row[3] != '':
                x.append(float(row[1]))
                y.append(float(row[2]))
                line_count += 1
    except TypeError:
        print('Brak plikow CSV')
    return x, y


# def motion_value(plots):
#     line_count = 0
#     y = []
#     for row in plots:
#         if line_count < 280:
#             line_count += 1
#         else:
#             if row[1] != '':
#                 y.append(float(row[2]))
#                 line_count += 1
#     return y
#
#
# def force_value(plots):
#     line_count = 0
#     y = []
#     for row in plots:
#         if line_count < 280:
#             line_count += 1
#         else:
#             if row[1] != '':
#                 y.append(float(row[1]))
#                 line_count += 1
#     return y



###########################
# Data Analysis
###########################

def Pomiar_sil(plots):
    max_force = float(data_separate(file_to_analizes())[8])
    max_force1=max_force*0.99
    line_count = 0
    row_count = 0
    stage1=0
    stage2=0
    z=0
    y = []
    x = []
    x1 = []
    y1 = []
    peak = 0
    for row in plots:
        if line_count <= 280:
            line_count += 1
            row_count += 1
        elif line_count > 280 and peak != 1:
                if z < max_force1:
                    z = round(float(row[2]),4)
                    y.append(z)

                    line_count += 1
                    row_count += 1
                    stage1 += 1
                    x.append(float(stage1))
                    # x.append(float(stage1))
                else:
                    peak=1
        elif row.__len__() > 2 and row[3] != '' and peak == 1 :
            g = round(float(row[2]), 4)
            y1.append(g)
            line_count += 1
            row_count += 1
            stage2 += 1
            x1.append(float(stage2))
            # x1.append(float(stage2))
    return x,y,x1,y1,max_force

def Delta_Force_Stage_1():

    strefa_1 = []
    strefa_2 = []
    strefa_11 = []
    strefa_22 = []
    stage1=0
    stage2=0
    change = 0
    przedzial = Pomiar_sil(file_to_analizes())[1]
    dzielnik = float(Pomiar_sil(file_to_analizes())[4])
    start_1 = float(data_separate(file_to_analizes())[11])
    zakres_I=start_1*0.15
    wychylenia1 = (dzielnik/(start_1*0.35))
    wychylenia2 = (dzielnik / (start_1 * 0.25))
    # print(dzielnik)
    # print(start_1)
    # print(wychylenia1)
    # print(wychylenia2)
    ostrze_I=0
    ostrze_II=0
    try:
        for w in range(len(przedzial)):
            if float(w) > 0:
                z = float(przedzial[w] - przedzial[w-1])
                round(z,4)
                if z < wychylenia1 and change != 1 or z >= wychylenia1 and stage1<=zakres_I:
                    strefa_1.append(float(round(z,4)))
                    stage1 += 1
                    strefa_11.append(float(stage1))
                    if abs(z) > 0.3*wychylenia1:
                        ostrze_I += 1
                elif z >= wychylenia1 and stage1>=zakres_I and change !=1:
                    change = 1
                elif change == 1:
                    strefa_2.append(float(round(z,4)))
                    stage2 += 1
                    strefa_22.append(float(stage2))
                    if abs(z) > 1.4*wychylenia2 or abs(z) < 0.7*wychylenia2:
                        ostrze_II += 1
        return strefa_1,strefa_11,strefa_2,strefa_22,ostrze_I, ostrze_II
    except IndexError:
        print('brak do przeliczenia liczb')
        return strefa_1,strefa_11,strefa_2,strefa_22,ostrze_I, ostrze_II

# def edge_sharpness_result():
#     a =Delta_Force_Stage_1()[2]
#     s = sum(a)
#     x = len(a)
#     m = float(s/x)
#     return m

def Analiza_Stref_I():

    strefa_1=Delta_Force_Stage_1()[4]
    if strefa_1 < 5:
        stan = 'ok'
        tlo = ' #00ff55 '
    elif strefa_1 <25:
        stan = 'umiarkowany'
        tlo = ' #ffff00 '
    else:
        stan = 'zły'
        tlo = ' #ff3300 '
    return stan,tlo


def Analiza_Stref_II():

    strefa_2=Delta_Force_Stage_1()[5]
    if strefa_2 < 5:
        stan = 'ok'
        tlo = ' #00ff55 '
    elif strefa_2 <25:
        stan = 'umiarkowany'
        tlo = ' #ffff00 '
    else:
        stan = 'zły'
        tlo = ' #ff3300 '
    return stan,tlo





# def plot_refresh(folder_path):
#     if watch_dog(folder_path) == True:
#         return False
#     else:
#         return True
