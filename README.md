## Web and Big Data Mining - Team G-Unit

An SJSU project by Somya, Jaewoong, and Ward

Dataset used: https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local

### Project Event Flow

![event-flow](images/event-flow.png)

### Instructions to run cli
- pip3 install -r requirements.txt
- gunzip --keep cli/usa_df_content.csv.gz > cli/usa_df_content.csv
- ./cli/gcli.py --location {"City, State" or "long, lat"} --categories {cat1, cat2}

### Examples:
- Example1: `./cli/gcli.py --location "Fort Lauderdale, FL" --categories sushi buffet`
<details>
<summary>Example1 output</summary>

  ![ex1](images/example1.png)

</details>

- Example2: `./cli/gcli.py --location "Bakersfield, CA" --categories indian buffet`
<details>
<summary>Example2 output</summary>

  ![ex2](images/example2.png)

</details>

  - Example3: `./cli/gcli.py --location "San Jose, CA" --categories american`
<details>
<summary>Example3 output</summary>

  ![ex3](images/example3.png)

</details>

  - Clear out the cached results: `./cli/clean.sh`

### Dependencies
- [Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Geoplot](https://residentmario.github.io/geoplot/quickstart/quickstart.html)
- [thampiman/reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
- [Rake nltk](https://pypi.org/project/rake-nltk/)
- [data/us_cities.csv](https://github.com/kelvins/US-Cities-Database)
