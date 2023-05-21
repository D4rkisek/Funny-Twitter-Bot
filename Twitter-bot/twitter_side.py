# Import the necessary library
import tweepy
from openai_side import generate_joke

# Create constants for keys and tokens
CONSUMER_KEY = 'consumer key'
CONSUMER_SECRET = 'consumer secret'
BEARER_TOKEN = r"bearer token"
ACCESS_TOKEN = 'access token'
ACCESS_TOKEN_SECRET = 'access token secret'

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def post_tweet(client, joke, hashtags=None):
    if hashtags:
        # Each hashtag will be prefixed with the '#' symbol
        joke += ' ' + ' '.join(['#' + tag for tag in hashtags])
    client.create_tweet(text=joke)

    print("Tweeted Successfully")
