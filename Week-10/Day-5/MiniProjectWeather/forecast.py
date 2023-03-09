from pyowm.owm import OWM

owm = OWM('f5d246278f5e139a1126a569d868bf58')
mgr = owm.weather_manager()
air_mgr = owm.airpollution_manager()


def init_plot():
    pass


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




retrive_weather_and_forecast()
