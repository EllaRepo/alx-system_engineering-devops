#!/usr/bin/python3
""" Defines recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles of all
       hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    if after:
        url += "&after={after}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data["data"]["after"])
    else:
        return('None')
