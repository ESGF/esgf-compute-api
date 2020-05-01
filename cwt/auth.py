import json
import os

class Authenticator(object):
    def __init__(self, **kwargs):
        self.loaded = False
        self.store = kwargs.pop('store', False)
        self.config_path = os.path.expanduser('~/.cwt.json')

        self.read()

    def write(self):
        with open(self.config_path, 'w') as fp:
            fp.write(json.dumps(self.to_dict()))

    def read(self):
        if os.path.exists(self.config_path):
            with open(self.config_path) as fp:
                data = fp.read()

            data = json.loads(data)

            try:
                self.from_dict(data)
            except Exception:
                pass
            else:
                self.loaded = True

    def clear(self):
        if os.path.exists(self.config_path):
            os.remove(self.config_path)

    def prepare(self, headers, query):
        if self.store and not self.loaded:
            self.write()

            self.loaded = True

    def from_dict(self, data):
        raise NotImplemented()

    def to_dict(self):
        raise NotImplemented()

class TokenAuthenticator(Authenticator):
    def __init__(self, token=None, key=None, value=None, **kwargs):
        self.token = token

        self.key = key or 'Authorization'

        self.value = value or 'Bearer {}'

        super().__init__(**kwargs)

    def from_dict(self, value):
        self.token = value['token']

    def to_dict(self):
        return {'token': self.token}

    def retrieve_token(self):
        return self.token

    def prepare(self, headers, query):
        self.token = self.retrieve_token()

        headers[self.key] = self.value.format(self.token)

        super().prepare(headers, query)
