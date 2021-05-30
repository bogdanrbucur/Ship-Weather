# Ship Weather

This tiny web app reads a ship's Vessel Finder "details" page from vesselfinder_link.txt, scrapes the geographical coordinates and opens Windy at the present time at those coordinates.

This is useful in finding out meteorological and hydrological conditions like wave height  and sea temperature which can not otherwise be accurately appreciated or measured by the navigator.

As of now the app is configured for one particular ship but can be changed to any ship by updating the link in the vesselfinder_link file.

In my implementation the app is deployed using Google Cloud Services and the changing of the vesselfinder_link file requires redeployment.

At its core it is a function that scrapes vesselfinder.com for the vessel's coordinates, formats them and contructs a URL to Windy.com using the coordinates as URL parameters. [Flask](https://github.com/pallets/flask) is used to turn the function into a web app.

It can also be compiled using [pyinstaller](https://github.com/pyinstaller/pyinstaller) after removing the Flask code and simply calling the function on launch.
