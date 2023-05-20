# Import the necessary library
import tweepy

# Create constants for keys and tokens
CONSUMER_KEY = 'your-consumer-key'
CONSUMER_SECRET = 'your-consumer-secret'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# Use the keys and tokens to authenticate with the Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create a variable api
api = tweepy.API(auth)


def post_tweet(joke):
    api.update_status(joke)


