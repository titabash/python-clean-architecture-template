import requests
import json


class HttpRequest:
    def __init__(self, endpoint, headers={"content-type": "application/json"}):
        self.endpoint = endpoint
        self.headers = headers
        pass

    def get(self, payload):
        res = requests.get(self.endpoint, headers=self.headers, params=payload)
        return res.json()

    def post(self, body):
        res = requests.post(self.endpoint, data=json.dumps(
            body), headers=self.headers)
        return res.json()


if __name__ == '__main__':
    print('--------------------GET Repuest--------------------')
    http_get_request = HttpRequest(
        endpoint="https://httpbin.org/get")
    print(http_get_request.get({'param1': 'hoge', 'param2': 1}))
    http_post_request = HttpRequest(
        endpoint="https://httpbin.org/post")
    print('--------------------POST Repuest--------------------')
    print(http_post_request.post({'param1': 'hoge', 'param2': 1}))
