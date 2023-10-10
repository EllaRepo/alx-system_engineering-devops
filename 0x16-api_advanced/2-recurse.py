#!/usr/bin/python3
""" Defines recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles of all
       hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts):
            hot_list.append(posts[0]['data']['title'])
        if not data['data']['after']:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data['data']['after'])
    else:
        return None
