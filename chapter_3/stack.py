
class StackWithMin(object):
    def __init__(self):
        self.storage = []
        self.min = []

    def push(self, value):
        self.storage.append(value)
        if len(self.min) == 0 or value < self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        popped = self.storage.pop()
        if self.min[-1] == popped:
            self.min.pop()
        return popped

    def get_min(self):
        if len(self.min) == 0:
            return None
        else:
            return self.min[-1]
