class Watcher:
    liczZ = 0
    """ A simple class, set to watch its variable. """
    def __init__(self, value):
        self.variable = value

    def set_value(self, new_value):
        if self.variable != new_value:
            # self.pre_change()
            self.variable = new_value
            self.post_change()
        return self.liczZ

    # def pre_change(self):
    #     self.liczZ -= 1
    #     return self.liczZ
        # do stuff before variable is about to be changed

    def post_change(self):
        global liczZ
        self.liczZ += 1
        print(self.liczZ)
        return self.liczZ

        # do stuff right after variable has changed


