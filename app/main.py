from core.target import Target
from core.context import Context
from core.session import Session
from core.crawler import Crawler
from core.detector import Detector


target = Target("http://localhost:9000")

session = Session(target)
context = Context()

crawler = Crawler(session, context)
crawler.crawl()

detector = Detector(session, target, context)
detector.run()

print(dict(context))

print(detector.results)
