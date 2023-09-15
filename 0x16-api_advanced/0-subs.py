#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to identify your application
    headers = {
        'User-Agent': 'MyRedditScraper/1.0 (by YourUsername)'
    }

    # URL to query for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']

            return subscribers
        else:
            # Request was not successful, return 0 for invalid subreddit
            return 0
    except Exception as e:
        # Handle exceptions (e.g., network errors)
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = 'learnpython'
subscribers = number_of_subscribers(subreddit_name)
if subscribers != 0:
