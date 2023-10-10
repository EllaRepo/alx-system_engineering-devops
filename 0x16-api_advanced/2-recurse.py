#!/usr/bin/python3
""" Defines recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
"""
import requests


def add_title(hot_list, posts):
    """ Adds item into a list """
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(hot_list, posts)


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
        add_title(hot_list, data['data']['children'])
        if not data['data']['after']:
            return hot_list
        else:
            return recurse(subreddit,
                           hot_list=hot_list,
                           after=data['data']['after'])
    else:
        return None
