from TwitterAPI import TwitterAPI


SEARCH_TERM = 'pizza'


CONSUMER_KEY = '7LxEHN7lW2zGQCZNcNZtuzdLq'
CONSUMER_SECRET = 'JQawZgy6limqZVSequyWGKuFvlBgDh4hcKY93GHWhjw4cmZmNM'
ACCESS_TOKEN_KEY = '902351089-6mmllKIUImkt2XpwUPCPUQWURfdKCTN2SA0YhLUP'
ACCESS_TOKEN_SECRET = '9xhdYntAMoSpqKeiIIWyCa92VGpWQojf7Oih9VMggfMVf'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)

print('\nQUOTA: %s' % r.get_rest_quota())
