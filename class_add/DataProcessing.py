import os, shutil, time


class DataMove:

    state = True

    def __init__(self, state):
        self.state = state


    def move_to_directory(self, path, moveto, freq):
        files = os.listdir(path)
        files.sort()
        # files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]
        # files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        # print(files[0])
        k = 0
        try:
            while self.state !=False and files.__len__() != k:
                # for f in files:

                src = path + files[k]
                dst = moveto + files[k]
                shutil.move(src, dst)
                k += 1
                time.sleep(freq)

        except FileNotFoundError:
            print('blad')



    def setState(self, newstate):
        self.state = newstate



