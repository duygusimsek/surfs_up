#Set up the Flask Weather App
#Add these dependencies
import datetime as dt
import numpy as np
import pandas as pd

#get the dependencies for SQLAlchemy, 
#which will help to access the data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import the dependencies that for Flask
from flask import Flask, jsonify

#set up the database engine for the Flask application
#Set up the Flask Weather App
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes.
Base = automap_base()

#to reflect the database
Base.prepare(engine, reflect=True)

#create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to the database
session = Session(engine)

#define the Flask app
app = Flask(__name__)

## Example of app name variable
# import app
# print("example __name__ = %s", __name__)
# if __name__ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported")

# Define welcome route
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''') 
##9.5.2 says to use flask run on the terminal

#Define the precipitation route
@app.route("/api/v1.0/precipitation")

def precipitaion():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitaion = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitaion}
    return jsonify(precip)
##check website changes, (http://127.0.0.1:5000/), should be block of dates

#Define the stations route
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all() #to create a query that will allow us to get all of the stations in our database
    stations = list(np.ravel(results)) #to start by unraveling our results into a one-dimensional array and convert our unraveled results into a list
    return jsonify(stations=stations) #jsonify the list and return it as JSON
##check website changes, (http://localhost:5000/), stations with USC0051xxxx codes

#Define the temperature observations for the previous year
@app.route("/api/v1.0/tobs")

#creating the function 
def temp_monthly():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365) #calculate the date one year ago from the last date in the database
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results)) #unravel the results into a one-dimensional array and convert that array into a list.
    return jsonify(temps=temps) #to jsonify the temps list, and return it.
##do flask run, (http://localhost:5000/), block of temps (F)

#to report on the minimum, average, and maximum temperatures(have to provide both a starting and ending date)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#define the function 
def stats(start=None, end=None):
    #to create a query to select the minimum, average, and maximum temperatures from our SQLite database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    ##to calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    #After running this code, you'll be able to copy and paste the web address provided by Flask into a web browser. 
    #Open /api/v1.0/temp/start/end route and check to make sure you get the correct result(which is [null,null,null])
    #This code tells us that we have not specified a start and end date for our range. 
    #Fix this by entering any date in the dataset as a start and end date. 
    #The code will output the minimum, maximum, and average temperatures
    #For example, let's say we want to find the minimum, maximum, and average temperatures for June 2017.
    #You would add the following path to the address in your web browser: '/api/v1.0/temp/2017-06-01/2017-06-30'
    #the return is ["temps":[71.0,77.21989528795811,83.0]]

## from tech help
# if __name__ == '__main__':
#     app.run()

