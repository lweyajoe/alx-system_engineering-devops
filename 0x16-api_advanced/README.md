# API advanced

More queries for APIs now, with the Reddit API.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files for all tasks. Provided by Holberton
School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File           | Prototype                               |
| -------------- | --------------------------------------- |
| `0-subs.py`    | `def number_of_subscribers(subreddit)`  |
| `1-top_ten.py` | `def top_ten(subreddit)`                |
| `2-recurse.py` | `def recurse(subreddit, hot_list=[])`   |
| `100-count.py` | `def count_words(subreddit, word_list)` |

## Tasks :page_with_curl:

* **0. How many subs?**
  * [0-subs.py](./0-subs.py): Python function that returns the total number of
  subscribers for a given subreddit.
  * Returns `0` if an invalid subreddit is given.

* **1. Top Ten**
  * [1-top_ten.py](./1-top_ten.py): Python function that prints the top ten
  hottest posts for a given subreddit.
  * Prints `None` if an invalid subreddit is given.

* **2. Recurse it!**
  * [2-recurse.py](./2-recurse.py): Python function that recursively returns a
  list of titles for all hot articles on a given subreddit.
  * Returns `None` if no results are found on the given subreddit.

* **3. Count it!**
  * [100-count.py](./100-count.py): Python function that recursively prints a
  sorted count of given keywords parsed from titles of all hot articles on a given
  subreddit.
  * Keywords are case-insensitive and delimited by spaces.
  * Results are printed in descending order by count.
  * Words with identical counts are sorted alphabetically.
  * Words with no matches are skipped.
  * Results are based on the number of times a keyword appears - ie.,
  `java java java` counts as three separate instances of `java`.


### Another way;

  <code>
  import requests

def get_subreddit_subscribers(subreddit):
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
subscribers = get_subreddit_subscribers(subreddit_name)
if subscribers != 0:

  </code>
