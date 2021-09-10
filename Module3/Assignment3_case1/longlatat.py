from math import radians, cos,sin,asin,sqrt
def distance(long_1,long_2,lat_1,lat_2):
    long_1 = radians(long_1)
    long_2 = radians(long_2)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    dist_long = long_2 - long_1
    dist_lat = lat_2 - lat_1
    a = sin(dist_lat/2) ** 2 + cos(lat_1) * cos(lat_2) * sin(dist_long/2) ** 2
    b = 2 *  asin(sqrt(a))
    r = 6371
    return(r*b)

lat_1 = float(input("Starting latitude:"))
lat_2 = float(input("Ending latitude: "))
long_1 = float(input("Starting longitude: "))
long_2 = float(input("Ending longitude: "))
print(distance(lat_1, lat_2, long_1, long_2), "KM")
