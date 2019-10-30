import requests
r = requests.get('https://www.reddit.com/r/politics/hot.json', headers={'User-Agent': '24abc24'})
d = r.json()

for i in range(10):
    try:
        print(str(i + 1) + ': ' + d.get('data').get('children')[i].get('data').get('title'))
    except AttributeError:
        print(None)