import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url=self.url
        response=requests.get(url)
        return response.content
        pass

    def load_json(self):
        items=json.loads(self.get_response_body())
        return items
    


        pass