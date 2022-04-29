# Surf-Up Analysis

## Overview 

### History 
The purpose of the previous analysis was to run some analysis on the weather dataset of the island of Oahu. To get investors to invest in opening a Surf N’ Shake shop, the weather year-round analysis was needed. 
To serve this purpose, the weather dataset (full-year data) was gathered from different stations, and the data was stored by using SQLite. By using SQLAlchemy the connection between the dataset and database (SQLite database) was achieved. 

To get a better understanding of the trends in the data, all of the station observations were displayed by a plot. In addition to the plot that was provided,  some solid statistical analyses—such as the mean, standard deviation, minimum, and maximum were calculated to get a summary of different statistics for the amount of precipitation in a year. The analysis of temperature was added and the result of the analysis was visualized. To share the results of those applications with others Flask web frame was used.
[climate_analysis.ipynb](https://github.com/duygusimsek/surfs_up/blob/main/climate_analysis.ipynb)

### Purpose of this Analysis
This analysis aimed to provide additional information about temperature trends on Oahu before opening the surf shop. The temperature data of Oahu island from the months of June and December was determined to find out if opening a Surf N’ Shake shop is conducive. 

## Result 




## Summary
By analyzing these two tables;

* The temperatures from the months of June and December show that the minimum temperature drops under 60 degrees, which is not desired degree for ice cream. Also, the warmest weathers for December are over 74 degrees, which is promising for investment.  Both months of June and December have a mean of over 71 degrees, which shows nice weather for surfing and ice cream.

* Expectedly, the June temperatures are higher than in December, with a maximum temperature of 83 and a minimum temperature of 64 degrees. 

* There is no major difference between the temperatures of June and December, and that can help to predict the weather of the Oahu island has consistent temperatures. 

* With this weather information, opening a Surf N’ Shake shop in Oahu is a good business venture. However, It might be useful to gather and analyze more data about the weather conditions of the location - such as wind speed and rainy days. 



## Resources 
* Data Source: [hawaii.sqlite](https://github.com/duygusimsek/surfs_up/blob/main/hawaii.sqlite)
* Software: [Visual Studio Code, 1.65.2](https://visualstudio.microsoft.com/downloads/),[Jupiter Notebook 6.3.0](https://jupyter.org/) 
* Language: [Python 3.10.2](https://www.python.org/downloads)
* Web Frame: Flask
* Libraries: Pandas, Numpy, Sqlalchemy, SQLite
