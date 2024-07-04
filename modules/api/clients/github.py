import requests


class GitHub:
    def __init__(self):
        self.base_url = "https://api.github.com"

    def get_user(self, username):
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url)
        return response.json()

    def search_repo(self, name):
        url = f"{self.base_url}/search/repositories"
        params = {'q': name}
        response = requests.get(url, params=params)
        return response.json()


 #Adding methods for working with Emoji and commits


    def get_emojis(self):
        url = f"{self.base_url}/emojis"
        response = requests.get(url)
        return response.json()

    def list_commits(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        response = requests.get(url)
        return response.json()
