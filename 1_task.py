import requests

marvel_heroes = ['Hulk', 'Captain_America', 'Thanos']


def smartest_hero(heroes):
    url = "https://superheroapi.com/api/2619421814940190/search/"
    result = {}
    for name in heroes:
        url_name = url + name
        response = requests.get(url_name).json()
        result[response['results'][0]['name']] = response['results'][0]['powerstats']['intelligence']
    the_smartest = max(sorted(result.items(), key=lambda x: x[1]))
    return the_smartest


if __name__ == '__main__':
    print(f'Самый умный герой {smartest_hero(marvel_heroes)[0]}, его интелект равен {smartest_hero(marvel_heroes)[1]}')
