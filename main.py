import requests


def get_intelligence():
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    intelligence = {}
    for item in response.json():
        if item['name'] in ('Hulk', 'Captain America', 'Thanos'):
            intelligence[item['powerstats']['intelligence']] = item['name']
    return intelligence[sorted(intelligence, reverse=True)[0]]


if __name__ == '__main__':
    print('Самый умный супергерой:', get_intelligence())
