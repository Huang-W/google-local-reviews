# cmpe256-team4

## Dataset
- [Link](https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local)

## Dependencies / starter-code used
- Ipynb from class ( surprise, titanic, data prep )
- [Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Geoplot](https://residentmario.github.io/geoplot/quickstart/quickstart.html)
- [thampiman/reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
- [Lenskit MultiEval starter code](https://github.com/lenskit/lkpy/blob/master/examples/MultiEval.ipynb)
- [Lenskit nDCG starter code](https://lkpy.lenskit.org/en/latest/GettingStarted.html)
- [Rake nltk](https://pypi.org/project/rake-nltk/)
- [data/us_cities.csv](https://github.com/kelvins/US-Cities-Database)

## setup
1. pip install virtualenv
2. virtualenv venv
3. source venv/bin/activate
4. pip install ipykernel
5. pip install reverse-geocoder
6. pip install geoplot
7. pip install rake-nltk
8. ipython kernel install --user --name=venv
9. jupyter lab
10. Open your Notebook with the newly created kernel!

## Instructions to run cli
- pip3 install scipy
- pip3 install pandas
- pip3 install sklearn
- python3 ./cli/gcli.py --location {"City, State" or "long, lat"} --categories {cat1, cat2}
- Example: `python3 cli/gcli.py --location "San Jose, CA" --categories barbecue`
