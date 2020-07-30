import requests


class BaseAPI:
    def _handle_call(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
        except Exception as err:
            print(err)
            raise err

        return response.json()


class TwitchAPI(BaseAPI):
    def twitch_api(self, method, url, **kwargs):
        return self._handle_call(method, url, **kwargs)
