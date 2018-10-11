from django.shortcuts import render
import json
import oauth2 as oauth
from .apps import TwitterapiConfig

#Function to call Twitter Api's
def callTwitterApi(endpoint):
    oauth_consumer = oauth.Consumer(key=TwitterapiConfig.consumer_key, secret=TwitterapiConfig.consumer_secret)
    oauth_token = oauth.Token(key=TwitterapiConfig.access_token, secret=TwitterapiConfig.access_token_secret)
    client = oauth.Client(oauth_consumer, oauth_token)

    timeline_endpoint = endpoint
    response, data = client.request(timeline_endpoint)
    return json.loads(data)

def getusertweets(request):
    timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Seekers Tweet&count=5"
    tweets = callTwitterApi(timeline_endpoint)

    for tweet in tweets:
        print('Tweet id : ', tweet['id'], 'Tweet Text :', tweet['text'])

    context = {'tweet': tweets}
    return render(request, 'TwitterApi/home.html', context)
