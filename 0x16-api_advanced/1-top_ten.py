#!/iusr/bin/python3
""" Contains a function that queries the Reddit API. """

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    user_agent = 'Mozilla/5.0'
    headers = {'user-agent': user_agent}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    param = {'limit': 10}
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
    children = data.get('data')['children']
    if len(children) < 1:
        print(None)
    else:
        for item in children:
            title = item.get('data').get('title')
            print(title)
