#!/usr/bin/env python3
import requests
import IPython
import json
import praw

if __name__ == "__main__":
    config = json.load(open("private/creds.json", "r"))
    reddit = praw.Reddit(client_id=config['oauth_id'], client_secret=config['secret'],
                             password=config['password'], user_agent='WOMPWOMP 0.1',
                                                  username=config['username'])
    subreddit = reddit.subreddit('buildapcsales')
    submissions = subreddit.new()
    for s in submissions:
        if 'monitor' in s.title.lower():
            print("Monitor submission: {} -> {}".format(s.title, s.url))
