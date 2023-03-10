from pyowm.owm import OWM
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
owm = OWM('f5d246278f5e139a1126a569d868bf58')
mgr = owm.weather_manager()
air_mgr = owm.airpollution_manager()


def init_plot():
    np.random.seed(3)
    x = 0.5 + np.arange(8)
    y = np.random.uniform(2, 7, len(x))

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))


    plt.show()


def retrive_weather_and_forecast():

    input_city = input('Enter a city that you wanna know weather and forecast: ')
    try:
        observation = mgr.weather_at_place(input_city)
        w = observation.weather
        hourly_forecast = mgr.forecast_at_place(input_city, '3h')
    except:
        raise "You entered invalid city"

    print(f'Current weather situation in {input_city}')
    print(f' - weather {w.detailed_status}')
    print(f' - winds speed {w.wind()["speed"]}')
    print(f" - sunrise time {w.sunrise_time(timeformat='date')}; sunset time {w.sunset_time(timeformat='date')}")
    print('Forecast for next hours:')
    for weather in hourly_forecast.forecast.weathers:
        print(f" - weather for {weather.reference_time('iso'), weather.statusTT}")




# retrive_weather_and_forecast()
init_plot()
