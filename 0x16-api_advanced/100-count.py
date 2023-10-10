#!/usr/bin/python3
""" Defines a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
"""
import requests
import re


def add_title(hot_list, posts):
    """ Adds item into a list """
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(hot_list, posts)


def count_words(subreddit, word_list, after=None, counts=None):
    """Queries the Reddit API, parses the title of all hot articles, and prints
       a sorted count of given keywords (case-insensitive, delimited by spaces
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
              'after': after,
              'limit': 100
              }
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if counts is None:
        counts = {}
    if response.status_code != 200:
        return
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            pattern = r"\b" + re.escape(word.lower()) + r"\b"
            matches = re.findall(pattern, title)
            if matches:
                if word.lower() in counts:
                    counts[word.lower()] += len(matches)
                else:
                    counts[word.lower()] = len(matches)
    next_page = data["data"]["after"]
    if next_page is not None:
        count_words(subreddit, word_list, after=next_page, counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
