# Clothing similarity and Google Cloud deployment
- This app can accept a string and return a json with top 5 matching clothing items.
- It is deployed on Google Cloud Functions

<br></br>

### File 1: `data_collection.py`
This file demonstrates how to scrape data from the web ([Bewakoof](https://www.bewakoof.com/) used here) and create a database (`fashion_data.csv` here).


### File 2: `main.py`
This file has the main functions and the function that has been deployed on Google Cloud Platform. Returns a json of 5 top-matching items.


### File 3: `test.py`
This file takes a query input from the user and calls the function api deployed on cloud returning a json response.

<br></br>

NOTE: This database is for demonstration purposes and does not have a huge database for matching, The code for web scaping is here and the size can be increased.