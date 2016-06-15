# fitness-data-lake
Main project for a general health data lake appliation

This prototype collects data from a user's FitBit device. The data will (hopefully) be used as part of a research
 study on the long-term outcomes of living kidney donors. Apple's Research Kit API provides an easy way to create
 research studies that reach more people and automatically collect relevant data. 
 
 This application is written in Django/Python and pushed to Pivotal Web Services via CloudFoundry.
 
 Current feature:
 
    * user authorization to pull data from fitbit - returns the user's profile in a webpage
 
 Future enhancments:
 
    * store access tokens and user data in some persistent storage
    * leverage FitBit Subscription API for auto-notification when user data is changed on FitBit server
    * create research study app for iPhones
        * "front-end" for this application
        * pull other data from iOS Health app, such as Nutrition details
    * analytics to review/analyze the stored data
