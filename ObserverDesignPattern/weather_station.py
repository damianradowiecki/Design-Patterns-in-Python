from observable import Observable


class WeatherStation(Observable):

    def __init__(self):
        self.observers = []
        self.weather = None

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def register_weather_change(self, weather):
        self.weather = weather
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.weather)
