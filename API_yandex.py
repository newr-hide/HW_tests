import requests


TOKEN_YA = "token"

url = "https://cloud-api.yandex.net/v1/disk/resources"

def create_folder_YA(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YA}
    create_fol = requests.api.put(url, headers=headers, params=params)
    print(create_fol.status_code)
    return create_fol.status_code

create_folder_YA('тест')
