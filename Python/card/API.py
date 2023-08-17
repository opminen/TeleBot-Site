import requests

class API:
    url = "http://localhost:8080/card/"

    @staticmethod
    def getAll():
        return requests.get(API.url).json()

    @staticmethod
    def get(id):
        return requests.get(f"{API.url}{id}").json()

    @staticmethod
    def post(name, text):
        return requests.post(API.url, json={"name": name, "text": text})

    @staticmethod
    def put(id, name, text):
        return requests.put(f"{API.url}{id}", json={"name": name, "text": text}).json()

    @staticmethod
    def delete(id):
        requests.delete(f"{API.url}{id}")
