import requests
class Api:
    def __init__(self,url,authkey):
        self.url = url
        self.token = authkey
    def servers(self):
        headers = {
            "Authorization": "Bearer {}".format(self.token),
            "Accept": "application/json"
        }
        response = requests.get("{}/api/client".format(self.url), headers=headers)
        self.result = response.json()
        return self.result
