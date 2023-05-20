# Import necessary libraries
import openai
import tweepy
import openai_side
from openai_side import generate_joke
import twitter_side
from twitter_side import CONSUMER_KEY, post_tweet


# Call the generate_joke function to get a joke and the post_tweet function to tweet the joke.
joke = generate_joke()
post_tweet(joke)
