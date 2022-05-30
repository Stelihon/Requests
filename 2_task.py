import requests
import os


class Yandex():
    def __init__(self, token):
        self.token = token

    def get_header(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def getting_a_link(self, link):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': link, 'overwrite': 'true'}
        headers = self.get_header()
        response = requests.get(link_url, headers=headers, params=params)
        return response.json().get('href', '')

    def upload_file(self, file_name):
        href = self.getting_a_link(os.path.basename(file_path))
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f'{file_name} успешно загружен')


if __name__ == '__main__':
    token = input('Введите токен: ')
    ya = Yandex(token)
    file_path = input('Введите путь к файлу: ')
    ya.upload_file(file_path)