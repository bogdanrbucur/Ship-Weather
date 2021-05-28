# Ship Weather

This tiny web app reads a ship's Vessel Finder "details" page from vesselfinder_link.txt, scrapes the geographical coordinates and opens Windy at the present time at those coordinates.

This is useful in finding out meteorological and hydrological conditions like wave height  and sea temperature which can not otherwise be accurately appreciated or measured by the navigator.

As of now the app is configured for the Bro Nibe but can be changed to any ship by updating the link in the vesselfinder_link file.

In my implementation the app is deployed with Google Cloud services and the changing of the vesselfinder_link file requires reployment.