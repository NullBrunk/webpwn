import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, session, context):
        self.session = session
        self.context = context
        self.target = self.session.target
        self.visited = set()
    
    
    def crawl(self, path="/"):
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


    def parse_links(self, soup, current_url):
        for link in soup.find_all("a", href=True):
            href = link["href"]

            absolute = urljoin(current_url, href)
            
            parsed = urlparse(absolute)

            # Vérification que l'URL est bien dans la scope
            if parsed.netloc and parsed.netloc != self.target.host:
                continue

            path = parsed.path or "/"
            self.context.add_endpoint(path, "GET")