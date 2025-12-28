"""
- endpoints découverts
- paramètres
- suspicions
- vulnérabilités confirmées
"""


class Context:
    def __init__(self):
        self.endpoints = {}
        self.params = {}
        self.suspicions = set()
        self.vulns = []

    def __iter__(self):
        yield "endpoints", {k: list(v) for k, v in self.endpoints.items()}
        yield "params", {k: list(v) for k, v in self.params.items()}
        yield "suspicions", list(self.suspicions)
        yield "vulns", self.vulns

    def items(self):
        return dict(self).items()

    def __repr__(self):
        return str(dict(self))