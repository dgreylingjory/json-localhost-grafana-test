# json-localhost-grafana-test
Program runs a random string generator and a random number generator, adds a timestamp and writes it into a JSON.
Not efficient for long term usage, only for proof of concept (the way it is designed will eat up memory).
It creates a periodic data source, that is later hosted on a local server (using json-server), with the hopes of later monitoring it on Grafana.

Steps to get json-server up:
    1. Install json-server:
        bash npm install -g json-server
    2. Run in folder where JSON file is, and set a port (default port is 3000, interferes with default grafana port -- I used port 6789 for no particular reason and it worked). Usage in this project is:
        bash json-server --watch db.json --port 6789
    At this point console will list the dictionaries as they are written, in a 1 second interval standard for this code. In web browser you can access localhost:6789 and it will show the same entries as in console, but you will be able to click each one and see the data.

Grafana JSON plugin:
    1. Install plugin, using grafana-cli.exe (in same directory where the other Grafana executables are). Using console in grafana\bin:
        bash grafana-cli plugins install simpod-json-datasource
    2. If Grafana is running, restart Grafana
    3. Add simpod-json-datasource as datasource in Grafana
    4. Dashboard -- TBD
