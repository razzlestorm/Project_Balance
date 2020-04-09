import newspaper
import random

sites = [
    'https://arstechnica.com/',
    'https://www.bbc.com/news/world',
    'https://www.c-span.org/',
    'https://www.cnet.com/',
    'https://www.defensenews.com/',
    'http://www.digitaljournal.com/',
    'https://www.afp.com/en/news-hub',
    'https://www.ft.com/',
    'https://news.gallup.com/home.aspx',
    'https://hbr.org/',
    'https://www.politico.com/',
    'https://www.reuters.com/',
    'https://www.pewresearch.org/',
    'https://www.economist.com/',
    'https://www.voanews.com/'
]

def create_site_dict(lst):
    site_dict = {}
    for ii in lst:
        source = newspaper.build(f'{ii}', memoize_articles=False)
        site_dict[ii] = [article.url for article in source.articles]
    return site_dict

site_dict = create_site_dict(sites)

#This flattens the list of lists that is site_dict.values()
feed = [article for sublist in site_dict.values() for article in sublist]

#this takes a long time
parsed = [newspaper.Article(ii).download() for ii in feed]

#randomfeed = random.sample(feed, len(feed))

#timefeed = feed.sort(key=lambda art:art.article.publish_date)

print(parsed)
