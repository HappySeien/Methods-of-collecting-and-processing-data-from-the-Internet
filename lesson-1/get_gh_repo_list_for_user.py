# 1. https://api.github.com/users/"USERNAME"/repos
import requests
# from pprint import pprint
import json as js


def get_gh_repo_list_for_user(username: str):
    """
    Принимает на вход имя пользователя github и возвращает список его репозиториев.
    сохраняет ответ в json
    """
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.ok:
        repo_list = []
        json_data = response.json()
        # pprint(json_data)

        with open(f'{username}_gh_repo_list.json', 'w') as f:
            js.dump(json_data, f)

        for i in json_data:
            repo_list.append(i['name'])

        return repo_list
    else:
        return response.status_code
    

if __name__ == '__main__':
    gh_repo_list = get_gh_repo_list_for_user('happyseien')
    print(gh_repo_list)