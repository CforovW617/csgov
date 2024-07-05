# /usr/bin/python
# -*- coding: utf-8 -*-
from scrapy import cmdline

# cmdline.execute("scrapy crawl xxgk -o xxgk.json -t json".split())
cmdline.execute("scrapy crawl leader_info -o leader_info.json -t json".split())