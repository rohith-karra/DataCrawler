## Project Abstract

The aim of this project is to create a dashboard so that users can navigata and interact with the analysis we have done so far. Flask is used to create this application. PostgreSQL is used as a database to connect and fetch the retrieved data.

## Team - Squad

* Rohith Reddy Karra, rkarra1@binghamton.edu
* Chanukya Vantipenta, cvantip1@binghamton.edu
* Vikash Eppela, veppela1@binghamton.edu
* Krishna Preetham Bhavirisetty, kbhavir1@binghamton.edu

## Tech-stack

* `Flask` - Flask is a web famework in python (https://github.com/pallets/flask)
* `VaderSentiment` -Used vader for our sentiment analysis
* `wordcloud`, `pandas`, `matplotlib`
* `python` - The project is developed and tested using python v3.8. [Python
Website](https://www.python.org/)
language. [Request Website](https://docs.python-requests.org/en/latest/#)
* `postgreSQL`- This project uses relationalDB postgreSQL for saving collected data.
* [PostgreSQL Website](https://www.postgresql.org/)
* [Python PostgreSQL Adapter - psycopg2](https://www.psycopg.org/)
* `twitter` - Popular social media platform and also a library that needs to be installed in python
* `reddit` - Reddit is a widely known application used for expressing opinions. Python also has seperate
library for it.

## Three data-source documentation

This section must include two things for each source: (1) A specific end-point URL(aka API) or Website
link if you are crawling web-pages (2) Documentation of the API

* `Twitter`
* [Sample Stream API]( https://developer.twitter.com/en/docs/twitter-api/v1/tweets/sample-
realtime/overview) - &lt;This is a streaming api which contains 1% of twitter data.&gt;
* `Reddit` - We are using `r/sports`.
* [r/sports]( https://www.reddit.com/r/sports/) - &lt;sports subreddit, we will be collecting data from
this&gt;
* [reddit api]( https://www.reddit.com/dev/api/)-> endpoint-> https://oauth.reddit.com/r/sports/new
* `YouTube` - &lt;we have chosen our third data source as youtube)
* [API-Link]( https://developers.google.com/youtube/v3) - &lt;Used this api to collect data&gt;( https://developers.google.com/youtube/v3)

## Web app HomePage
 * ![alt text](https://github.com/2022-Fall-CS-415-515/project-3-implementation-squad/blob/master/flaskapp/static/images/homepage.png)
 

## Analysis in our homepage
* Timeseries plot for twitter, user can change start date and end date to get updated plot
* sentiment analysis on three platforms
* wordcloud 
* data dumper (it fetches the rows from our database based on user input. for eg. if user wants to check the posts which are on football they can type the text and select in which paltform they want the data to fetch from)

## How to run the project?

Install `Python`, `PostgreSQL`, `psycopg2`,`flask` `wordcloud` ,`pandas`,`matplotlib` 

To run flask app:

• Go to project directory and open terminal

• In terminal enter this command==> FLASK_APP=app.py FLASK_ENV=development flask run

• Go to browser and enter http://127.0.0.1:5000

To run from VM:
• Go to flaskapp directory ("~/flaskapp)
• Enter this command to start server==> FLASK_APP=app.py flask run –host 0.0.0.0
• Go to browser and run http://128.226.28.119:5000

TO connect to db please change the username and password if needed.

