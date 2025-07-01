import logging
from requests import request


class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}
        response = request("GET", url, headers=headers, data=payload)
        self.log.info(f"Get Method")
        self.log.info(f"URL: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def post_method(self, url, payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}
        response = request("POST", url, headers=headers, data=payload)
        self.log.info(f"POST Method")
        self.log.info(f"URL: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def put_method(self, url, payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}
        response = request("PUT", url, headers=headers, data=payload)
        self.log.info(f"PUT Method")
        self.log.info(f"URL: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code


    def patch_method(self, url, payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}
        response = request("PATCH", url, headers=headers, data=payload)
        self.log.info(f"PATCH Method")
        self.log.info(f"URL: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code


    def delete_method(self, url, payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}
        response = request("DELETE", url, headers=headers, data=payload)
        self.log.info(f"DELETE Method")
        self.log.info(f"URL: {url}")
        self.log.info(f"headers: {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code


