from urllib.parse import urlparse

"""
Responsabilité

- URL
- scope
- headers
- cookies
- stack supposée
"""

class Target:
    def __init__(self, url):
        self.url = url.rstrip("/")
        self.parsed = urlparse(self.url)

        self.scheme = self.parsed.scheme
        self.host = self.parsed.netloc
        self.base = f"{self.scheme}://{self.host}"

        self.headers = {}
        self.cookies = {}
        self.stack = []

    def add_header(self, key, value):
        self.headers[key] = value

    def add_cookie(self, key, value):
        self.cookies[key] = value

    def add_stack(self, tech):
        if tech not in self.stack:
            self.stack.append(tech)

    def __iter__(self):
        yield "url", self.url
        yield "parsed", self.parsed
        yield "scheme", self.scheme
        yield "host", self.host
        yield "base", self.base
        yield "headers", {k: list(v) for k, v in self.headers.items()}
        yield "cookies", {k: list(v) for k, v in self.cookies.items()}
        yield "stack", self.stack

    def items(self):
        return dict(self).items()

    def __repr__(self):
        return str(dict(self))