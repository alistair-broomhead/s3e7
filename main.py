__author__ = 'Team # (Alistair Broomhead, x y z)'

from flaskext.oauth import OAuth

consumer_key='NxQb0nVZZpnaokDjgUURLg', #TODO#
consumer_secret='5a9SBrLxvYkYp3xv462Y2N1t2FSkUurGgqD4w9qwU' #TODO#

AccessToken = "510810904-yperFxEfqHoGLpF5nPsW8adTOdm1BX9pZbumcuvQ"
AccessSecret = "OnNjP7pQjgEW6OJOBI7lUMfnkQIF7GNTkCkPuoLA"

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
