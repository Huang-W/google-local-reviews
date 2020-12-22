## cmpe256 - team g-unit

Dataset used: https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local

### Dependencies
- [Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Geoplot](https://residentmario.github.io/geoplot/quickstart/quickstart.html)
- [thampiman/reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
- [Rake nltk](https://pypi.org/project/rake-nltk/)
- [data/us_cities.csv](https://github.com/kelvins/US-Cities-Database)

### Instructions to run cli
- pip3 install scipy
- pip3 install pandas
- pip3 install sklearn
- pip3 install sqlalchemy
- pip3 install geopy
- gunzip --keep cli/usa_df_content.csv.gz > cli/usa_df_content.csv
- python3 ./cli/gcli.py --location {"City, State" or "long, lat"} --categories {cat1, cat2}

Included CLI examples:
- Example1: `python3 ./cli/gcli.py --location "Fort Lauderdale, FL" --categories sushi buffet`
- Example2: `python3 ./cli/gcli.py --location "Bakersfield, CA" --categories indian buffet`
- Example3: `python3 ./cli/gcli.py --location "San Jose, CA" --categories american`
- Clear out the cached results: `./cli/clean.sh`

### Event Flow

![event-flow](images/event-flow.png)
