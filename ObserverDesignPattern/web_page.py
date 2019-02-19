from observer import Observer


class WebPage(Observer):

    def __init__(self):
        self.data = ''

    def update(self, data):
        self.data = data
        print('WebPage: ' + str(self.data))
