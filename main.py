__author__ = 'Team # (Alistair Broomhead, x y z)'

import oauth2 as oauth

consumer_key='NxQb0nVZZpnaokDjgUURLg', #TODO#
consumer_secret='5a9SBrLxvYkYp3xv462Y2N1t2FSkUurGgqD4w9qwU' #TODO#

CONSUMER_KEY = 'NxQb0nVZZpnaokDjgUURLg'
CONSUMER_SECRET = '5a9SBrLxvYkYp3xv462Y2N1t2FSkUurGgqD4w9qwU'
CONSUMER = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

ACCESS_TOKEN_FILE = 'OAUTH_ACCESS_TOKEN'

TWITTER_REQUEST_TOKEN_URL = 'http://twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'http://twitter.com/oauth/access_token'
TWITTER_AUTHORIZE_URL = 'http://twitter.com/oauth/authorize'
TWITTER_STREAM_API_HOST = 'stream.twitter.com'
TWITTER_STREAM_API_PATH = '/1/statuses/sample.json'

def build_access_token():
    return oauth.Token(key=str_key, secret=str_secret)

def build_authorization_header(access_token):
    url = "https://%s%s" % (TWITTER_STREAM_API_HOST, TWITTER_STREAM_API_PATH)
    params = {
        'oauth_version': "1.0",
        'oauth_nonce': oauth.generate_nonce(),
        'oauth_timestamp': int(time.time()),
        'oauth_token': access_token.key,
        'oauth_consumer_key': CONSUMER.key
    }

    # Sign the request.
    # For some messed up reason, we need to specify is_form_encoded to prevent
    # the oauth2 library from setting oauth_body_hash which Twitter doesn't like.
    req = oauth.Request(method="GET", url=url, parameters=params, is_form_encoded=True)
    req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), CONSUMER, access_token)

    # Grab the Authorization header
    header = req.to_header()['Authorization'].encode('utf-8')
    print "Authorization header:"
    print "     header = %s" % header
    return header

def main():
    oauth = OAuth()
    twitter = oauth.remote_app('twitter',
        base_url='http://api.twitter.com/1/',
        request_token_url='http://api.twitter.com/oauth/request_token',
        access_token_url='http://api.twitter.com/oauth/access_token',
        authorize_url='http://api.twitter.com/oauth/authenticate',
        consumer_key='NxQb0nVZZpnaokDjgUURLg', #TODO#
        consumer_secret='5a9SBrLxvYkYp3xv462Y2N1t2FSkUurGgqD4w9qwU' #TODO#
    )


if __name__ == "__main__":
    main()