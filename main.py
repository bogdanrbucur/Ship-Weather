from urllib.request import Request, urlopen
from flask import Flask, redirect
# import webbrowser  # legacy code for .exe

app = Flask(__name__)


def windy_link():
    # Read the ship's Vesselfinder.com page. This can be changed for any other ship
    with open('vesselfinder_link.txt', 'r') as reader:
        vessel_link = reader.read()

    req = Request(vessel_link, headers={'User-Agent': 'Mozilla/5.0'})
    # opens the link and retrieves the HTML code
    html_bytes = urlopen(req).read()
    html = html_bytes.decode("utf-8")
    # grabs the line which contains the vessel's coordinates. It starts after the word "coordinates"
    start_index = html.find('coordinates') + 12
    end_index = start_index + 23
    coordinates = html[start_index:end_index]

    if coordinates.find('N') != -1:  # if there's a 'N', then the coordinates are N
        lat_index = coordinates.find('N')
        lat = coordinates[:lat_index - 3]
        lat = lat.replace(' ', '')  # removes blanks from the coordinate
    else:
        lat_index = coordinates.find('S')
        lat = coordinates[:lat_index - 3]
        lat = lat.replace(' ', '')
        lat = '-' + lat  # prefixes the lat with - for S

    if coordinates.find('E') != -1:  # if there's an 'E', then the coordinates are E
        long_index = coordinates.find('E')
        long = coordinates[long_index - 10:long_index - 3]
        long = long.replace(' ', '')  # removes blanks or / characters from the coordinate
        long = long.replace('/', '')
    else:
        long_index = coordinates.find('W')
        long = coordinates[long_index - 10:long_index - 3]
        long = long.replace(' ', '')  # removes blanks or / characters from the coordinate
        long = long.replace('/', '')
        long = '-' + long  # prefixes the long with - for W

    # print(coordinates)
    # print(lat)
    # print(long)

    # Windy URL arguments: lat/long/info_type(meteogram, waves, etc)?lat,long,zoom_level
    weather_link = "https://www.windy.com/" + lat + "/" + long + "/meteogram?" + lat + "," + long + ",6"

    # webbrowser.open(weather_link, new=0, autoraise=True)  # legacy code for .exe

    return weather_link


@app.route('/')
def index():
    return redirect(windy_link())  # immediately redirects to weather_link returned by windy_link()
    # return "<h1>Some header here</h1>"  # for HTML


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
