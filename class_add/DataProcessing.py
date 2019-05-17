import os, shutil, time


class DataMove:

    state = True

    def __init__(self, state):
        self.state = state


    def move_to_directory(self, path, moveto, freq):
        files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=False)
        k = 0
        try:
            while self.state !=False and files.__len__() != k:
                x = files[k]
                b = x.split('//')
                src = path + b[1]
                dst = moveto + b[1]
                shutil.move(src, dst)
                k += 1
                time.sleep(freq)

        except FileNotFoundError:
            print('blad')



    def setState(self, newstate):
        self.state = newstate



