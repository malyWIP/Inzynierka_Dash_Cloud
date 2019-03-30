import os, shutil, time


class DataDel:

    state = True

    def __init__(self, state):
        self.state = state


    def move_to_directory(self, path, moveto):

        files = os.listdir(path)
        files.sort()
        k = 0
        try:
            while self.state is not False and files.__len__() != k:
                src = path + files[k]
                dst = moveto + files[k]
                shutil.move(src, dst)
                k += 1
                time.sleep(0.01)

        except FileNotFoundError:
            print('blad')



    def setState(self, newstate):
        self.state = newstate



