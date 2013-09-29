#!/usr/bin/env python
import os

from lumeizhi import Crawler, image_download


if not os.path.isdir("./data"):
    os.mkdir("data")

c = Crawler(0, 10)
mm_no = 1

for elem in c.crawl():
    mm_name = "MM" + str(mm_no)
    image_file_name = mm_name + ".jpg"
    image_url = "http://lumeizhi.com" + elem["src"]

    print "Now we are on the way to meet " + mm_name
    image_download(image_url, image_file_name)

    mm_no += 1
