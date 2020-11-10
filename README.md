# cmpe256-team4

## Libraries used / Sample starter code
- Ipynb from class ( surprise, titanic, data prep )
- [Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Geoplot](https://residentmario.github.io/geoplot/quickstart/quickstart.html)
- [thampiman/reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
- [Lenskit MultiEval starter code](https://github.com/lenskit/lkpy/blob/master/examples/MultiEval.ipynb)
- [Lenskit nDCG starter code](https://lkpy.lenskit.org/en/latest/GettingStarted.html)
- [Surprise](https://surprise.readthedocs.io/en/stable/index.html)

## [Original data-sets](https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local)
- data/users.clean.json
- data/places.clean.json
- data/reviews.clean.json

## Original data-sets split into multiple files
- places/
- reviews/
- reviews_restaurants/
- users/

## Additionally added datasets
- [data/us_cities.csv](https://github.com/kelvins/US-Cities-Database)
- data/joined_df

## Subsets of above datasets after processing
- data/us_cities_rg.csv
- data/usa_df.csv
- data/only_restaurants_review.csv

## setup
1. pip install virtualenv
2. virtualenv venv
3. source venv/bin/activate
4. pip install ipykernel
5. pip install reverse-geocoder
6. pip install geoplot
7. ipython kernel install --user --name=venv
8. jupyter lab
9. Open your Notebook with the newly created kernel!
