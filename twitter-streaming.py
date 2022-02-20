import datetime
import json
import pymongo
import requests_oauthlib
import tqdm
import os
import yaml as Yaml

with open('twitter.yaml') as f:
	yaml = Yaml.load(f, Loader=Yaml.FullLoader)

	# key from twitter developers site
	consumer_key = yaml['CONSUMER_KEY']
	consumer_secret = yaml['CONSUMER_SECRET']
	access_token_key = yaml['ACCESS_TOKEN_KEY']
	access_token_secret = yaml['ACCESS_TOKEN_SECRET']

# Execute twitter streaming api
twitter = requests_oauthlib.OAuth1Session(
	consumer_key, consumer_secret, access_token_key, access_token_secret
)

uri = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = twitter.get(uri, stream=True)
r.raise_for_status()

# save sample twitter to mongodb
mongo = pymongo.MongoClient()
for line in tqdm.tqdm(r.iter_lines(), until='tweets', mininterval=1):
	if line:
		tweet = json.loads(line)
		# add timestamp
		tweet['_timestamp'] = datetime.datetime.utcnow().isoformat()
		mongo.twitter.sample.insert_one(tweet)
		print(tweet)
