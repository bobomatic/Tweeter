import tweepy
import time as t
import sys
import pprint
import os

# grab first argument of command line using sys
try:
    search_string = sys.argv[1]
except IndexError:
    print('Please specify a topic to search')


def authenticate():
    """Authenticate tweepy api using access keys and tokens from keys.txt"""
    try:
        with open('keys.txt', mode='r') as file:
            line = file.readline()
            consumer_key = line.strip().split('consumer_key=')[1]
            line = file.readline()
            consumer_secret = line.strip().split('consumer_secret=')[1]
            line = file.readline()
            auth_set_access_token = line.strip().split('auth_set_access_token=')[1]
            line = file.readline()
            access_token_secret = line.strip().split('access_token_secret=')[1]
            print(consumer_key, consumer_secret, auth_set_access_token, access_token_secret)
    except tweepy.TweepError as e:
        print(e.reason, '/n Please check keys.txt is present in current directory and try again.')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(auth_set_access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


api = authenticate()
user = api.me()


# Print my twitter details
print('\nMy Twitter Details:')
print('username: ', user.name, 'screen_name: ', user.screen_name, 'followers: ',
      user.followers_count)

# Print out tweets on my timeline
public_tweets = api.home_timeline()
print(f'\nMost recent tweets on my timeline: (first 5 of {len(public_tweets)})')
for i, tweet in enumerate(public_tweets):
    print(f'{tweet.user.screen_name}\n{tweet.text}')
    if i == 5:
        break


def limit_handler(cursor):
    """If twitter request rate limit error occurs, sleep for a while then try again"""
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        print('waiting on rate limit...')
        t.sleep(300)
    # new behaviour in 3.7 - StopIteration error raised when generator reaches last item
    except StopIteration:
        return


# Generous bot (refollow a follower)
print('\nFOLLOWERS:')
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.screen_name, end=', ')
    if follower.screen_name == 'bluemoonunit':  # could put any criteria here
        follower.follow()

# List friends
print('\n\n FRIENDS:')
for friend in limit_handler(tweepy.Cursor(api.friends).items(1)):  # only do 1 item for now
    print(friend.screen_name, end=', ')
print('\n')


def top_5_tweets(search_string, numberOfTweetsToSearch):
    """Return a list of popular tweets about search_string. 
    Optional: retweet or favourite the top tweets"""
    tweets = []
    hashed_tweets = []
    url = ""
    print(f'Searching for popular tweets about {search_string} ...\n')
    tweepy_search = tweepy.Cursor(api.search, search_string).items(numberOfTweetsToSearch)
    for i, tweet in enumerate(limit_handler(tweepy_search)):
        try:
            if tweet.favorite_count > 5 or tweet.retweet_count > 2000:
                # print(tweet, '\n') #debug: print out the json status object
                # check not a duplicate
                if not hashed_tweets.count(hash(tweet.text)):
                    # find url in tweet or retweet dict=entities key="urls"
                    if hasattr(tweet, "retweeted_status"):
                        entities = tweet.retweeted_status.entities
                        user = tweet.retweeted_status.user
                    else:
                        entities = tweet.entities
                        user = tweet.user
                    if "urls" in entities:
                        for ent in entities["urls"]:
                            if ent is not None:
                                if "url" in ent:
                                    url = ent["url"]
                    tweets.append({'id': tweet.id, 'screen_name': user.screen_name,
                                  'text': tweet.text,
                                   'url': url,                                 
                                   'created_at': tweet.created_at,
                                   'retweet_count': tweet.retweet_count,
                                   'favorite_count': tweet.favorite_count})
                    hashed_tweets.append(hash(tweet.text))
                    # optional: retweet or favourite the top tweet
                    # tweet.favorite()
                    # tweet.retweet(tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            print('Stop_iteration occurred!')
            break
        except AttributeError as e:
            # if no retweeted status try and continue?
            print(e)
    return tweets


# sort tweets by retweets and print the top 5
for i, tweet in enumerate(sorted(top_5_tweets(search_string, 100),
                                 reverse=True, key=lambda k: k['retweet_count'])):
    if i == 10:
        break
    print(f'{tweet}\n')
