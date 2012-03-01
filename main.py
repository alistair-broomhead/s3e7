__author__ = 'Team # (Alistair Broomhead, x y z)'

'''
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

'''


import oauth2 as oauth
import time
import requests
from oauth_hook import OAuthHook
import simplejson as json
import luhn
import re

consumer_key='NxQb0nVZZpnaokDjgUURLg', #TODO#
consumer_secret='5a9SBrLxvYkYp3xv462Y2N1t2FSkUurGgqD4w9qwU' #TODO#

access_token = "510810904-yperFxEfqHoGLpF5nPsW8adTOdm1BX9pZbumcuvQ"
access_token_secret = "OnNjP7pQjgEW6OJOBI7lUMfnkQIF7GNTkCkPuoLA"

mentions_url = "https://api.twitter.com/1/statuses/mentions.json"

pattern = re.compile(r'[^\d]*(\d+)[\d]*')

#def build_access_token():
#    return oauth.Token(key="510810904-yperFxEfqHoGLpF5nPsW8adTOdm1BX9pZbumcuvQ", secret="OnNjP7pQjgEW6OJOBI7lUMfnkQIF7GNTkCkPuoLA")
#
#def build_authorization_header(access_token):
#    params = {
#        'oauth_version': "1.0",
#        'oauth_nonce': oauth.generate_nonce(),
#        'oauth_timestamp': int(time.time()),
#        'oauth_token': access_token.key,
#        'oauth_consumer_key': CONSUMER.key
#    }
#
#    # Sign the request.
#    # For some messed up reason, we need to specify is_form_encoded to prevent
#    # the oauth2 library from setting oauth_body_hash which Twitter doesn't like.
#    req = oauth.Request(method="GET", url=url, parameters=params, is_form_encoded=True)
#    req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), CONSUMER, access_token)
#
#    # Grab the Authorization header
#    header = req.to_header()['Authorization'].encode('utf-8')
#    print "Authorization header:"
#    print "     header = %s" % header
#    return header

def main():
    oauth_hook = OAuthHook(access_token, access_token_secret, consumer_key, consumer_secret, True)
    client = requests.session(hooks={'pre_request': oauth_hook})
    response = client.get('https://api.twitter.com/1/search.json?q=ldnpydojo')
    print response
    results = json.loads(response.content)
    tweets = results['results']
    for tweet in tweets:
        tweet_text = tweet['text']
        print tweet_text
        try:
            clean_tweet = pattern.search(tweet_text).group(1)
            print "Tweet Num: %s" % clean_tweet
            is_luhn = luhn.is_luhn_valid(clean_tweet)
            print "Luhn: %s" % `is_luhn`
            if is_luhn:
                import pprint
                print "Tweet:"
                pprint.pprint(tweet)
                tweet_back = 'RT @%(user)s %(tweet)s'%{'user':tweet['from_user'], 'tweet':tweet['text']}
                print "Should Tweet back:", tweet_back
                response2 = client.post('http://api.twitter.com/1/statuses/update.json', {'status': tweet_back})
                print response2
        except:
            pass

if __name__ == "__main__":
    main()
