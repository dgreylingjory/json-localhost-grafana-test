# json-localhost-grafana-test
Program runs a random string generator and a random number generator, adds a timestamp and writes it into a JSON.
Not efficient for long term usage, only for proof of concept (the way it is designed will eat up memory).
It creates a periodic data source, that is later hosted on a local server (using json-server), with the hopes of later monitoring it on Grafana.

Steps to get json-server up:
    1. Install json-server:
        bash npm install -g json-server
    2. Run in folder where JSON file is, and set a port (default port is 3000, interferes with default grafana port -- I used port 6789 for no particular reason and it worked). Usage in this project is:
        bash json-server --watch db.json --port 6789
    At this point console will list the dictionaries as they are written, in a 2 second interval standard for this code. In web browser you can access localhost:6789 and it will show the same entries as in console, but you will be able to click each one and see the data.

Grafana plugins:
    1. Install Grafana Infinity plugin https://grafana.com/docs/plugins/yesoreyeram-infinity-datasource/latest/
    2. Use plugin as datasource in dashboard
    3. In query, use JSON API url, in my case http://localhost:6789/metrics
    4. Setup dashboard as needed (in my case, using transformation tool so Grafana would translate the timestamp from a string to a time field)
