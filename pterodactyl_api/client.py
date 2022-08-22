import requests
class server:
    def __init__(self):
        self.allocation = []
    def setName(self,name):
        self.name = name
    def isOwner(self,boolean):
        self.owner = boolean
    def addPORT(self,port):
        self.allocation.append(port)

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
        try:
            self.result = response.json()
        except:
            raise Exception(response.text)
        lista = []
        for i in self.result["data"]:
            if i["object"] == "server":
                temp = server()
                temp.setName(i["attributes"]["name"])
                temp.isOwner(i["attributes"]["server_owner"])
                for e in i["attributes"]["relationships"]["allocations"]["data"]:
                    temp.addPORT(e["attributes"]["port"])
                lista.append(temp)
        return lista

