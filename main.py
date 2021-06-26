from urllib.request import Request, urlopen
from flask import Flask, redirect, render_template, request

# import webbrowser  # legacy code for .exe

app = Flask(__name__)


def windy_link(vessel_link):
    try:
        # Read the ship's Vesselfinder.com page. This can be changed for any other ship
        # with open('vesselfinder_link.txt', 'r') as reader:  # legacy code to read from a text file
        #     vessel_link = reader.read()

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

        # Windy URL arguments: lat/long/info_type(meteogram, waves, etc)?lat,long,zoom_level,i:pressure(for isobars)
        weather_link = "https://www.windy.com/" + lat + "/" + long + "/meteogram?" + lat + "," + long + ",6,i:pressure"

        # webbrowser.open(weather_link, new=0, autoraise=True)  # legacy code for .exe

        return weather_link
    except:
        print('Cannot access VesselFinder.')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ship', methods=['GET', 'POST'])  # Bro Nibe
def ship():
    ship_name = request.form["button"]
    if 'Bro Nibe' in ship_name:
        page = 'https://www.vesselfinder.com/vessels/BRO-NIBE-IMO-9322700-MMSI-220495000'
        return redirect(windy_link(page))  # immediately redirects to weather_link returned by windy_link()
        pass
    elif 'Bro Nissum' in request.form["button"]:
        page = 'https://www.vesselfinder.com/vessels/BRO-NISSUM-IMO-9340623-MMSI-220504000'
        return redirect(windy_link(page))  # immediately redirects to weather_link returned by windy_link()
        pass
    elif 'Bro Agnes' in request.form["button"]:
        page = 'https://www.vesselfinder.com/vessels/BRO-AGNES-IMO-9348302-MMSI-564057000'
        return redirect(windy_link(page))  # immediately redirects to weather_link returned by windy_link()
        pass
    elif 'Maersk Maru' in request.form["button"]:
        page = 'https://www.vesselfinder.com/vessels/MAERSK-MARU-IMO-9581447-MMSI-563087300'
        return redirect(windy_link(page))  # immediately redirects to weather_link returned by windy_link()
        pass
    elif 'Maersk Cebu' in request.form["button"]:
        page = 'https://www.vesselfinder.com/vessels/MAERSK-CEBU-IMO-9786176-MMSI-219393000'
        return redirect(windy_link(page))  # immediately redirects to weather_link returned by windy_link()
        pass
    elif 'Maersk Kaya' in request.form["button"]:
        page = 'https://www.vesselfinder.com/vessels/MAERSK-KAYA-IMO-9431288-MMSI-566030000'
        return redirect(windy_link(page))  # immediately redirects to weather_link returned by windy_link()
        pass


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
