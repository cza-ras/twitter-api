import tweepy.client
import yaml

# Define your API keys
with open('twitter-api/secrets.yaml', 'r') as file:
    config = yaml.safe_load(file)


#Authenticate with the Clientś [with free account now you only can create tweets]
client = tweepy.Client(
    consumer_key=config['twitter_credentials']['CONSUMER_KEY'], consumer_secret=config['twitter_credentials']['CONSUMER_SECRET'],
    access_token=config['twitter_credentials']['ACCESS_TOKEN'], access_token_secret=config['twitter_credentials']['ACCESS_SECRET']
    )

print(f"Zalogowano jako {client.get_me().data['username']}")


# with free account now you only can create tweets
tweet = "Post created with free API. Might delete later"
client.create_tweet(text=tweet)