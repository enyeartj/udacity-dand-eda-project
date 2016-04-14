# Exploratory Data Analysis with R Project

This is the fourth project for the Udacity Data Analyst Nanodegree. This project
focuses on the skills taught in the [Data Analysis with
R](https://www.udacity.com/course/data-analysis-with-r--ud651)
course.

For the project, we were given a list of datasets to work with or had
the option to choose our own. I did a bit of both. I went with the suggested
Financial Contributions to Presidential Campaigns for a single state. I chose
the state of Nevada because that is where I live. The data comes directly from
the Federal Election Commission’s
[website](http://fec.gov/disclosurep/pnational.do).
There are 15,026 campaign contributions in the dataset to 21 presidential
candidates. There are 18 variables that characterize each contribution, such as
the contribution amount and the name, employer, city, and zip code of the
contributor. I also added income and population data downloaded from the [US
Census Bureau](http://factfinder.census.gov/faces/nav/jsf/pages/download_center.xhtml)
website and scraped from
[Wikipedia](https://en.wikipedia.org/wiki/List_of_cities_in_Nevada).

The scraping was done with [dataScraping.py](https://github.com/enyeartj/udacity-dand-eda-project/blob/master/dataScraping.py).

The R source code for the project is in [campaignFinance.Rmd](https://github.com/enyeartj/udacity-dand-eda-project/blob/master/campaignFinance.Rmd).

The project report can be viewed in HTML form here:
http://htmlpreview.github.io/?https://github.com/enyeartj/udacity-dand-eda-project/blob/master/campaignFinance.html