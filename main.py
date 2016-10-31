#!/usr/bin/python

import tweepy
import csv
import datetime

# Set up authentication
key = "fJG3F2SdcV9AyA07VgXELfYHp"
secret = "fp9VyzsrZBgdhaBeELitLb4m9RP23pezwn6PNC4PhxDw4fgBox"

user_token = "240373788-SzMNoJDFNRZxbZ7vwXtA4p75OjmQ4hRc4UstVEds"
user_secret = "nMb5TX0kYac8mKJH6RWHOITaf386u6QUSxqVo51UHHgR8"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(user_token, user_secret)

# Authenticate
api = tweepy.API(auth)

user = api.verify_credentials()

print("Connected to twitter, hello %s" % (user.name))

# Set up the search and results variables
results = None
search_term = ""
search_location = ""

# Get user input
search_term = raw_input("Please enter a search term (search terms should be separated by spaces, and can include hashtags): ")
using_location = raw_input("Do you want to search for tweets within a specified area? (y/n): ")

if using_location == "y":

    search_lat = raw_input("Please enter a latitude e.g. 37.760723 (Fukushima): ")
    search_long = raw_input("Please enter a longitude e.g. 140.473356 (Fukushima): ")
    search_radius = raw_input("Please enter a search radius in miles (Sorry, Twitter is American): ")

    search_location = search_lat+","+search_long+","+search_radius+"mi"
elif using_location == "n":
    None


# More input to see if we want to break after a certain number of tweets
return_limit = int(raw_input("How many tweets should I pull back? (typing 0 will tell me to keep going until I reach my api limit): "))

# Open a file and write the results
with open("results_%s.csv" % datetime.datetime.now(),"w") as results_file:
    fieldnames = ["user", "tweet", "timestamp"]
    writer = csv.DictWriter(results_file, fieldnames=fieldnames)
    writer.writeheader()

    # Fire off the search query here
    tweet_count = 1
    for tweet in tweepy.Cursor(api.search, q=search_term, geocode=search_location, count=200).items():
         print("Processing tweet %d" % tweet_count)
         writer.writerow({"user": tweet.user.screen_name.encode('utf8'), "tweet": tweet.text.encode('utf8'), "timestamp": tweet.created_at})

         # perform the check
         if tweet_count > return_limit and return_limit != 0:
             break

         tweet_count = tweet_count + 1


print("Complete")
