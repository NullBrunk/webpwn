"""
- gérer cookies
- headers
- auth plus tard
"""

import requests

class Session:
    def __init__(self, target):
        self.target = target
        self.session = requests.Session()

    def get(self, path, **kwargs):
        return self.session.get(
            self.target.base + path,
            headers=self.target.headers,
            cookies=self.target.cookies,
            **kwargs
        )

    def post(self, path, data=None, **kwargs):
        return self.session.post(
            self.target.base + path,
            data=data,
            headers=self.target.headers,
            cookies=self.target.cookies,
            **kwargs
        )
