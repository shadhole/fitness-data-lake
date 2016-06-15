# FitBit methods to get authorization code, access token, and refresh token
import base64
import urllib
import urllib.request
from django.http import HttpResponse
import json

#FitBit constants for our app after registering it on dev.fitbit.com
fitbit_client = '227MC6'
fitbit_secret = '3319aecdf8370a6b42c8559ea08d9bcb'
fitbit_auth_URL = 'https://www.fitbit.com/oauth2/authorize'
fitbit_token_URL = 'https://api.fitbit.com/oauth2/token'
fitbit_redirect_URI = 'http://fdl.cfapps.io/fitbit/auth'
fitbit_response_type = 'code'

#FitBit API endpoints for various data
fitbit_profile_API = "https://api.fitbit.com/1/user/-/profile.json"

'''
fitbit_activity_API
fitbit_sleep_API
fitbit_steps_API
fitbit_hearrate_API
'''

def getfitbit_token(auth_code):
    #build the body
    req_body = {'code' : auth_code,
                'redirect_uri' : fitbit_redirect_URI,
                'client_id' : fitbit_client,
                'grant_type' : 'authorization_code'}

    BodyURLEncoded = urllib.parse.urlencode(req_body).encode('utf-8')
    #print (BodyURLEncoded)

    #Start the request
    req = urllib.request.Request(fitbit_token_URL,BodyURLEncoded)

    #Add the headers, first we base64 encode the client id and client secret with a : inbetween and create the authorisation header
    fitbit_auth_string = fitbit_client + ":" + fitbit_secret
    fitbit_bytes = fitbit_auth_string.encode('utf-8')
    req.add_header('Authorization', 'Basic ' + base64.b64encode(fitbit_bytes).decode('ascii'))
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')

    #Fire off the request
    try:
      response = urllib.request.urlopen(req)

      FullResponse = response.read()

#      return "success! token is: " + FullResponse.decode('ascii')
      return FullResponse

    except urllib.error.URLError as e:
      return "error: " + e.message

def getfitbit_data(URL, auth_data):

    req = urllib.request.Request(URL)

    #Add the access token in the header
    json_response = json.loads(auth_data.decode('ascii'))
    AccToken = json_response['access_token']
    req.add_header('Authorization', 'Bearer ' + AccToken)

#    print "I used this access token " + AccToken
    #Fire off the request
    try:
      #Do the request
      response = urllib.request.urlopen(req)
      #Read the response
      FullResponse = response.read()

      #Return values
      return FullResponse
    #Catch errors, e.g. A 401 error that signifies the need for a new access token
    except urllib.error.URLError as e:
      #print "Got this HTTP error: " + str(e.code)
        HTTPErrorMessage = e.read()
        #print "This was in the HTTP error message: " + HTTPErrorMessage
        #See what the error was
        if (e.code == 401) and (HTTPErrorMessage.find("Access token invalid or expired") > 0):
            return e.message
        else:
            #Return that this didn't work, allowing the calling function to handle it
            return e.message


def subscribe_user(auth_code):
    #main logic that calls subroutines in this module

    '''
    the prototype passess the authorization Response data and returns the user profile as a string.
    ultimately, the authorization data and user data needs to be stored in some persistent storage
    and we need to use FitBit's SubscribeAPI to receive notifications when relevant data  - steps,
    activity, exercise, sleep - has been updated on FitBit's server for our users
    '''

    #use the auth_code to get the tokens needed to access user data
#    access_data = HttpResponse()
    try:
        auth_data = getfitbit_token(auth_code)
    except urllib.error.URLError as e:
        return "error getting authorization token: " + e.message

    #get user data
    try:
        fitbit_data = getfitbit_data(fitbit_profile_API ,auth_data)
        return fitbit_data.decode('ascii')
    except urllib.error.URLError as e:
        return "error getting user data: " + e.message


