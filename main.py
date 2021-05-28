from urllib.request import Request, urlopen
# import webbrowser  # legacy code for .exe
from flask import Flask, redirect, url_for

app = Flask(__name__)


def weather_link():
    # Read the ship's Vesselfinder.com link. This can be changed for any other ship
    with open('vesselfinder_link.txt', 'r') as reader:
        vessel_link = reader.read()

    req = Request(vessel_link, headers={'User-Agent': 'Mozilla/5.0'})
    html_bytes = urlopen(req).read()
    html = html_bytes.decode("utf-8")

    start_index = html.find('coordinates') + 12
    end_index = start_index + 23
    coordinates = html[start_index:end_index]

    if coordinates.find('S') == -1:  # checks if the latitude is N or S
        is_north = True
    else:
        is_north = False

    if coordinates.find('W') == -1:  # checks if the longitude is E or W
        is_east = True
    else:
        is_east = False

    if is_north:
        lat_index = coordinates.find('N')
        lat = coordinates[:lat_index - 3]
        lat = lat.replace(' ', '')   # removes blanks from the coordinate
    else:
        lat_index = coordinates.find('S')
        lat = coordinates[:lat_index - 3]
        lat = lat.replace(' ', '')
        lat = '-' + lat  # prefixes the lat with - for S

    if is_east:
        long_index = coordinates.find('E')
        long = coordinates[long_index - 10:long_index - 3]
        long = long.replace(' ', '')  # removes blanks or / characters from the coordinate
        long = long.replace('/', '')
    else:
        long_index = coordinates.find('W')
        long = coordinates[long_index - 10:long_index - 3]
        long = long.replace(' ', '')    # removes blanks or / characters from the coordinate
        long = long.replace('/', '')
        long = '-' + long  # prefixes the long with - for W

    # print(coordinates)
    # print(lat)
    # print(long)

    weather_link = "https://www.windy.com/" + lat + "/" + long + "/waves?" + lat + "," + long + ",6"

    # webbrowser.open(weather_link, new=0, autoraise=True)  # legacy code for .exe

    return weather_link


@app.route('/')
def index():
    return redirect(weather_link())  # Immediately redirects to weather_link
    # return "<h1>Some header here</h1>"  # for HTML


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
