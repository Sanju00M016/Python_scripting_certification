from geopy.geocoders import Nominatim
import time
from pprint import pprint

location = Nominatim(user_agent='Name_of_location')
loc = location.geocode('Abbigere').raw
pprint(loc)