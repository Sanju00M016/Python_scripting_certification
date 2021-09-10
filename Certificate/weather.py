from pytz import timezone
from pyowm import OWM

my_key = '3250858df42308da39d1adb3b0acf32b'
wm = OWM(my_key).weather_manager()

location = input('Enter Location for Weather Details: ')
weather = wm.weather_at_place(location).weather

print('------------------------------------------')
print('City Weather Details:', str.upper(location))
print('------------------------------------------')

print('Current Weather:', weather.detailed_status)

print('Temperature:', weather.temperature('celsius').get('temp'), 'deg celsius')
print('Min Temperature:', weather.temperature('celsius').get('temp_min'), 'deg celsius')
print('Max Temperature:', weather.temperature('celsius').get('temp_max'), 'deg celsius')

print('Wind Speed:', weather.wind().get('speed'), 'metres per second')
print('Humidity:', weather.humidity, '%')
print('Number of clouds:', weather.clouds)

print('Pressure:', weather.pressure.get('press'))
print('Sunrise:', weather.sunrise_time(timeformat='date').astimezone(timezone('Asia/Singapore')).strftime('%X'))
print('Sunset:', weather.sunset_time(timeformat='date').astimezone(timezone('Asia/Singapore')).strftime('%X'))