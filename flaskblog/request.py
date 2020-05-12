import urllib.request,json
from .models import Quote

request_url = 'http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    with urllib.request.urlopen(request_url) as url:
        response = json.loads(url.read())

        id = response['id']
        author = response['author']
        quote = response['quote']
        permalink = response['permalink']

        return Quote(id,author,quote,permalink)
