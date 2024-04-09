#!/usr/bin/python3
""""""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.

    Returns:
        The number of subscribers (int) for the given subreddit. If the subreddit is invalid, returns 0.
    """
    # Construct the URL for the Reddit API endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Define custom headers with a User-Agent to prevent "Too Many Requests" error
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Send an HTTP GET request to the API endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the subreddit is invalid (status code 404)
    if response.status_code == 404:
        return 0
    
    # Parse the JSON response and extract the number of subscribers
    results = response.json().get("data")
    return results.get("subscribers")

if __name__ == "__main__":
    # If script is run directly, retrieve subreddit name from command-line argument
    import sys
    
    # Check if a subreddit name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call number_of_subscribers function with the provided subreddit name
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

