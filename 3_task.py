import requests
import datetime as dt
from time import sleep


def query_search(tag):
    result = []
    url = "https://api.stackexchange.com/2.3/questions?page="
    date = f'{dt.date.today() - dt.timedelta(days=2)}'
    page = 1
    while True:
        need_url = f'{url}{page}&pagesize=100&fromdate={date}&order=asc&sort=creation&tagged={tag}&site=stackoverflow'
        response = requests.get(need_url)
        response_json = response.json()
        for item in response_json['items']:
            result.append(item['title'])
        if not response_json['has_more']:
            break
        page += 1
        sleep(1)
    return result


if __name__ == '__main__':
    print(len(query_search('Python')))
    print(*query_search('Python'), sep='\n')

