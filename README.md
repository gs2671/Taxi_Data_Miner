<img src = "https://static-s.aa-cdn.net/img/ios/641194843/e2ba076c9daa930271c0be22ed5318e7" align = "right">

# Trends and Customer Segmentation analysis on Citi-bike in New York City


The Citi Bike, a public bicycle sharing system that serves parts of New York City, is the largest bike-sharing program in the United States. With the existing wealth of data pertaining to Citi Bike users in New York City, it is possible to identify and categorize the customer domain based on several factors such as Age, Sex, and Seasons which will help the company to identify their potential customers that can be targeted and also, how the weather and seasons affect the business. It is also possible to identify hot-spot locations and peak-demand hours, which can be crucial information that can help the company to better manage the demand and supply. Identifying various ways to help in driving more revenue. 

Dataset Used
==============
The dataset that will be used for the analysis includes trip data from all trips completed by yellow Taxis and Citi Bike in NYC from 2013 to 2015 and also, weather data in NYC from 2013 to 2015. 


Findings
==============
* Neighbourhood Trends - Citi Bike
* Citi bike Customer segmentation 
* Taxi pickups and drop off location affecting the Citi Bike
* Yellow Taxi vs Citi Bike Travel time 
* Hot-spot locations and peak-demand hours
* Weather affecting the business
* Trends during various seasons

API Used
==============
1) Weather Data
```bash
https://www.wunderground.com/history/airport/KNYC/{}/{}/{}/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=5&reqdb.wmo=99999&format=1
```

2) Citibike DataSet 
```bash
https://s3.amazonaws.com/tripdata/index.html
```

3) Citibike Live Status
```bash
https://www.citibikenyc.com/stations/json
```

4) Google Distance
```bash
http://maps.googleapis.com/maps/api/distancematrix/json?origins= orig_coord&destinations= dest_coord&mode=bicycling&language=en-EN&sensor=false
```

Project Team
==============
* Vignesh Ramesh
* Guruprasad Srinivasamurthy
* Jay M Patel


