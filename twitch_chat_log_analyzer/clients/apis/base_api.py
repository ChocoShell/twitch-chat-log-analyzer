import requests


class BaseAPIException(Exception):
    pass


class BaseAPI:
    def _handle_call(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
        except Exception as err:
            print(err)
            raise BaseAPIException(err)

        return response
