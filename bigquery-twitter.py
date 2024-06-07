import yaml
import os
import tweepy
from datetime import date


# Define your API keys
with open('twitter-api/secrets.yaml', 'r') as file:
    config = yaml.safe_load(file)


#Authenticate with the API
auth = tweepy.OAuthHandler(config['twitter_credentials']['CONSUMER_KEY'], config['twitter_credentials']['CONSUMER_SECRET'])
auth.set_access_token(config['twitter_credentials']['ACCESS_TOKEN'], config['twitter_credentials']['ACCESS_SECRET'])
api = tweepy.API(auth)
print(f"Zalogowano jako : {api.verify_credentials().screen_name}")

#Define accounts to reteive data
# konta = ["Platforma_org", "pisorgpl", "KONFEDERACJA_", "nowePSL", "PL_2050", "__Lewica"]

# for konta in konta:
#     dane = api.get_user(screen_name=konta)
#     wiersz_z_danymi = [{"User": konta, "Followers": str(dane.followers_count)}]
#     print(wiersz_z_danymi)