# Ship Weather

This web app reads a ship's Vessel Finder "details" page, scrapes the geographical coordinates and opens Windy at the present time at those coordinates.

This is useful in finding out meteorological and hydrological conditions like wave height  and sea temperature which can not otherwise be accurately appreciated or measured by the navigator.

In my implementation the app is deployed using Google Cloud Services and changing the ships or adding new ones required re-deployment as the buttons are in the HTML file and the ships' Vessel Finder pages are in main.py which require re-uploading.

The  page uses [Bootstrap](https://github.com/twbs/bootstrap) for reactive design and should look fine on any screen size. I use a custom.css for customization. The color palette is also dark mode friendly for browsers that support it.

At its core it is a function that scrapes vesselfinder.com for the vessel's coordinates, formats them and contructs a URL to Windy.com using the coordinates as URL parameters. [Flask](https://github.com/pallets/flask) is used to turn the function into a web app.