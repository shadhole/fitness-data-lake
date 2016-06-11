# FitBit methods to get authorization code, access token, and refresh token
import base64
import urllib

from django.http import HttpResponse

#FitBit constants for our app after registering it on dev.fitbit.com
fitbit_client = '227MC6'
fitbit_secret = '3319aecdf8370a6b42c8559ea08d9bcb'
fitbit_auth_URL = 'https://www.fitbit.com/oauth2/authorize'
fitbit_token_URL = 'https://api.fitbit.com/oauth2/token'
fitbit_redirect_URI = 'http://fdl.cfapps.io/fitbit/auth'
fitbit_response_type = 'code'

def getfitbit_token(auth_code):
    #build the body
    req_body = {'code' : auth_code,
                'redirect_uri' : fitbit_redirect_URI,
                'client_id' : fitbit_client,
                'grant_type' : 'authorization_code'}

    BodyURLEncoded = urllib.urlencode(req_body)
    print (BodyURLEncoded)

    #Start the request
    req = urllib.request.Request(TokenURL,BodyURLEncoded)

    #Add the headers, first we base64 encode the client id and client secret with a : inbetween and create the authorisation header
    req.add_header('Authorization', 'Basic ' + base64.b64encode(fitbit_client + ":" + fitbit_secret))
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')

    #Fire off the request
    try:
      response = urllib.request.urlopen(req)

      FullResponse = response.read()

      return "success! token is: " + FullResponse

    except urllib.error.URLError as e:
      return "error: " + e.message
