from weather_station import WeatherStation
from web_page import WebPage
from television_station import TelevisionStation

weather_station = WeatherStation()

weather_station.add(WebPage())
weather_station.add(TelevisionStation())

weather_station.register_weather_change('weather changed 1')
weather_station.register_weather_change('weather changed 2')
weather_station.register_weather_change('weather changed 3')
weather_station.register_weather_change('weather changed 3')
