from abc import ABC


class Observable(ABC):

    def add(self, observer):
        pass

    def remove(self, observer):
        pass

    def notify(self):
        pass
