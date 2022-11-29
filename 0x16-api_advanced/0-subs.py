#!usr/bin/python3
'''Contains a function that queries the Reddit API.'''

import requests


def number_of_subscribers(subreddit):
    '''queries the Reddit API and returns the number of subscribers for a given
    subreddit
    '''
    user_agent = 'Mozilla/5.0'
    headers = {'user-agent': user_agent}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    data = res.json()
    if 'data' not in data:
        return 0
    subscribers = data['data'].get('subscribers', None)
    if not subscribers:
        return 0
    return subscribers
