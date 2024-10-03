class Stack():
    def __init__(self):
        self.ints = []

    def push(self, val):
        self.ints.append(val)

    def pop(self, remove=False):
        last = self.ints[-1]

        if remove:
            self.ints = self.ints[:-1]

        return last

    def __str__(self):
        return str(self.ints)