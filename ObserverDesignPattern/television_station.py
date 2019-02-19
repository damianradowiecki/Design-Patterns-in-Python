from observer import Observer


class TelevisionStation(Observer):

    def __init__(self):
        self.data = ''

    def update(self, data):
        self.data = data
        print('TV: ' + str(self.data))
