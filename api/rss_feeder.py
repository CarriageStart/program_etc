
import json
import requests
import feedparser


def main():
    query = "머신러닝"
    url = "https://news.google.com/rss/search?q=%s&&hl=ko&gl=KR&ceid=KR:ko" % query
    rss_news = feedparser.parse(url)

    title = rss_news["feed"]["title"]
    updated = rss_news["feed"]["updated"]
    print(f"{title=}")
    print(f"{updated=}")


if __name__=="__main__":
    print("Execute main function")
    main()
    print("Fisnish main function")




