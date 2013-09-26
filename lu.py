#!/usr/bin/env python
import os

from lumeizhi import Crawler, image_download


if "data" not in os.listdir("."):
    os.mkdir("data")

c = Crawler(0, 10)
mm_no = 1

for elem in c.crawl():
    image_name = "MM" + str(mm_no) + ".jpg"
    image_url = "http://lumeizhi.com" + elem["src"]
    print "Now we are on the way to meet " + image_name
    image_download(image_url, image_name)

    mm_no += 1
