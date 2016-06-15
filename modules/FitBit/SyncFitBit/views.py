from django.shortcuts import render
from django.http import HttpResponse
from . import fitbit_auth

# Create your views here.

def index(request):
    # the context variables are used to build the href block in index.html
    # it is not working fully in the html code, but doesn't need to be commented out here.
    context = { 'fitbit_auth' : fitbit_auth.fitbit_auth_URL,
                'fitbit_response' : fitbit_auth.fitbit_response_type,
                'fitbit_client' : fitbit_auth.fitbit_client,
                'fitbit_secret' : fitbit_auth.fitbit_secret,
                'fitbit_redirect_URI' : fitbit_auth.fitbit_redirect_URI
                }
    return render(request, "SyncFitBit/index.html", context)

def auth(request):
    #this will be where we parse the auth code, request the access/refresh tokens
    # and make the fitbit api calls

    auth_code = request.GET.get('code')

    context = { 'fitbit_auth_code' : fitbit_auth.subscribe_user(auth_code)}
    return render(request, "SyncFitBit/auth.html", context)