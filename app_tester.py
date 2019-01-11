import os, shutil, time

global state



def move_to_directory(path, moveto, freq, value):
    state = True
    files = os.listdir(path)
    files.sort()
    # print(files[0])
    k = 0
    try:
        while value!=0 and files.__len__() != k:
            # for f in files:

            src = path + files[k]
            dst = moveto + files[k]
            shutil.move(src, dst)
            k += 1
            time.sleep(freq)

    except FileNotFoundError:
        print('blad')


# if __name__ == '__main__':
#     path = r'D:\STUDIA\Inżynierka\test\\'
#     moveto = r'D:\STUDIA\Inżynierka\testowy\\'
#     freq = 0.1
#     move_to_directory(path, moveto, freq, 1)