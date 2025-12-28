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

    def add_endpoint(self, path, method="GET"):
        self.endpoints.setdefault(path, set()).add(method)

    def add_param(self, path, param):
        self.params.setdefault(path, set()).add(param)

    def add_suspicion(self, vuln_type):
        self.suspicions.add(vuln_type)

    def add_vuln(self, vuln):
        self.vulns.append(vuln)

    def __iter__(self):
        yield "endpoints", {k: list(v) for k, v in self.endpoints.items()}
        yield "params", {k: list(v) for k, v in self.params.items()}
        yield "suspicions", list(self.suspicions)
        yield "vulns", self.vulns

    def items(self):
        return dict(self).items()

    def __repr__(self):
        return str(dict(self))