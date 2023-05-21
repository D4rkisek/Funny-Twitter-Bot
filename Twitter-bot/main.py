from openai_side import generate_joke
from twitter_side import post_tweet, client
from bot import hashtags

if __name__ == '__main__':
    joke = generate_joke()
    post_tweet(client, joke, hashtags)
