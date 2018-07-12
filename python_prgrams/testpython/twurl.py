#http://www.pythonlearn.com/html-008/cfbook014.html
import urllib
from oauth import oauth
#import oauth
import hidden

def augment(url, parameters) :
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'],secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, 
        token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()


#https://api.twitter.com/1.1/statuses/user_timeline.json?count=2&oauth_version=1.0&oauth_token=778022415720849408-hV2dgItqL5hH65uzkAjtXd5UK01c5pg&screen_name=drchuck
