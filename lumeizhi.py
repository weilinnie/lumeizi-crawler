import os
import urllib
import urllib2
import json

json_2b_api = "http://lumeizhi.com/image.json"


class Crawler(object):

    def __init__(self, page=0, limit=50):
        self.page_value = page
        self.limit_value = limit

    def page(self, page):
        self.page_value = page
        return self

    def limit(self, limit):
        self.limit_value = limit
        return self

    def fetch_page(self):
        request_url = json_2b_api + "?" + \
            "limit=" + str(self.limit_value) \
            + "&offset=" + str(self.page_value)
        response_data = urllib2.urlopen(request_url).read()
        image_lists = json.loads(response_data)

        return image_lists

    def crawl(self):
        while True:
            r = False
            for elem in self.fetch_page():
                r = True
                yield elem
            self.page_value += self.limit_value
            if not r:
                break


def image_download(url, image_name):
    cureent_dir = os.path.dirname(os.path.abspath(__file__))
    urllib.urlretrieve(url, cureent_dir + "/data/" + image_name)
