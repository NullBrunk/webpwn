import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, session, context, max_depth=5):
        self.session = session
        self.context = context
        self.target = self.session.target
        self.visited = set()
        self.max_depth = max_depth
    
    def crawl(self, path="/", depth=None):
        if depth is None:
            depth = self.max_depth

        if depth <= 0:
            return

        current_url = self.target.base + path

        if path in self.visited:
            return

        self.visited.add(path)

        try:
            response = self.session.get(path, timeout=5)
        except Exception:
            return

        if not response or "text/html" not in response.headers.get("Content-Type"):
            return

        self.context.add_endpoint(path, "GET")

        soup = BeautifulSoup(response.text, "html.parser")

        self.parse_links(soup, current_url)
        self.parse_forms(soup, current_url)

        for endpoint in list(self.context.endpoints.keys()):
            if endpoint not in self.visited:
                self.crawl(endpoint, depth - 1)



    def parse_links(self, soup, current_url):
        for link in soup.find_all("a", href=True):

            href = link["href"]

            absolute = urljoin(current_url, href)
            
            parsed = urlparse(absolute)
            if parsed.scheme and parsed.scheme not in ("http", "https"):
                continue

            # Vérification que l'URL est bien dans la scope
            if parsed.netloc and parsed.netloc != self.target.host:            
                continue

            path = parsed.path or "/"
            self.context.add_endpoint(path, "GET")


    def parse_forms(self, soup, current_url):
        for form in soup.find_all("form"):
            action = form.get("action", "")
            method = form.get("method", "GET").upper()
            
            absolute = urljoin(current_url, action)

            parsed = urlparse(absolute)
            if parsed.scheme and parsed.scheme not in ("http", "https"):
                continue

            # Vérification que l'URL est bien dans la scope
            if parsed.netloc and parsed.netloc != self.target.host:
                continue

            path = parsed.path or "/"
            self.context.add_endpoint(path, method)



            # Récupération des inputs
            for input_tag in form.find_all("input"):
                name = input_tag.get("name")
                if name:
                    self.context.add_param(path, name)