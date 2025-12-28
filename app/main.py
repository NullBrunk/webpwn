from core.target import Target
from core.context import Context
from core.session import Session
from core.crawler import Crawler

target = Target("http://localhost")

session = Session(target)
context = Context()

crawler = Crawler(session, context)

crawler.crawl()

print(dict(context))