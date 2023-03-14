import requests

def consultaGithub (login):
    url = f"https://api.github.com/users/{login}"
    response=requests.get(url)
    if response.status_code == 200:
        dados = response.json()
    else:
        dados = ''
    return dados