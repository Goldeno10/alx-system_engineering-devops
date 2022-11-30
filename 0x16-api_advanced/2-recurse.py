#!/usr/bin/python3
""" Contains a function that queries the Reddit API. """
import requests


def add_title_to_list(hot_posts, hot_list):
    """ Add post titles to a list. """
    if len(hot_posts) == 0:
        return hot_list
    else:
        hot_list.append(hot_posts[0].get('data').get('title'))
        hot_posts.pop(0)
        add_title_to_list(hot_posts, hot_list)


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    user_agent = 'Mozilla/5.0'
    headers = {'user-agent': user_agent}
    param = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=headers,
                       params=param,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    data = res.json()
    if 'data' not in data:
        print(None)
        return
    if 'children' not in data.get('data'):
        print(None)
        return
    hot_posts = data.get('data').get('children')
    add_title_to_list(hot_posts, hot_list)
    after = data.get('data').get('after')
    print(after)
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
