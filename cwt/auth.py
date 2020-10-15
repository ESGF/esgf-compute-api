import json
import os

class Authenticator(object):
    def __init__(self, config_path=None, store=False):
        self.store = store
        self.config_path = config_path or os.path.expanduser("~/.cwt.json")
        self.data = {}

        self.read()

    def write(self):
        with open(self.config_path, 'w') as fp:
            fp.write(json.dumps(self.data))

    def read(self):
        if os.path.exists(self.config_path):
            with open(self.config_path) as fp:
                data = fp.read()

            self.data = json.loads(data)

    def clear(self):
        self.data = {}

        self.write()

    def prepare(self, key, headers, query):
        if key in self.data:
            stored_headers = self.data[key]["headers"]

            stored_query = self.data[key]["query"]
        else:
            stored_headers, stored_query = self._pre_prepare()

            self.data[key] = {
                "headers": stored_headers,
                "query": stored_query,
            }

            self.write()

        headers.update(stored_headers)

        query.update(stored_query)

class TokenAuthenticator(Authenticator):
    def __init__(self, token=None, key=None, value=None, **kwargs):
        self.token = token

        self.key = key or 'Authorization'

        self.value = value or 'Bearer {}'

        super().__init__(**kwargs)

    def retrieve_token(self):
        return self.token

    def _pre_prepare(self):
        token = self.retrieve_token()

        headers = {
            self.key: self.value.format(token)
        }

        return headers, {}
