import fitbit
import datetime

client_key = '227MC6'
client_secret = '3319aecdf8370a6b42c8559ea08d9bcb'
oAuth_url = 'https://www.fitbit.com/oauth2/authorize'
oAuth_token_url = 'https://api.fitbit.com/oauth2/token'

auth_client = fitbit.uti
s = auth_client.get_sleep(datetime.date(2016,05,20))
print "sleep data: " + s