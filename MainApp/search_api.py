import requests


def call_api(url):
    """
    Makes a call to a URL, and sends data for 'results' key from json object
    """
    response = make_request(url)
    if response[0] == 'success':
        data = response[1].json()
        if 'results' in data:
            return data['results']
    elif response[0] == 'connection error':
        return 'Connection Error'


# HELPER FUNCTION
def make_request(url):
    """
    Make request to an URL
    :param url: any url
    :return: success and response if successful, otherwise error
    """
    try:
        return 'success', requests.get(url)
    except requests.exceptions.ConnectionError:
        return 'connection error', None


class SearchAPI:
    """
    This class holds on to Apple's search and lookup urls.
    Allows to search specific artist(term) or lookup an id.
    """

    def __init__(self):
        self.api_search_url = "https://itunes.apple.com/search?"
        self.api_lookup_url = "http://itunes.apple.com/lookup?"

    def search_artist(self, term):
        url = self.make_search_url(term)
        return call_api(url)

    def lookup_id(self, given_id):
        url = self.api_lookup_url + "id=" + given_id
        return call_api(url)[0]

    # HELPER FUNCTION
    def make_search_url(self, term):
        return self.api_search_url + "term="+"+".join(term.split()) + \
               "&entity=musicTrack"
