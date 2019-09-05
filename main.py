# from scrapy.cmdline import execute
#
# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "itcast"])

from scrapy import cmdline
cmdline.execute("scrapy crawl itcast -o teachers.csv".split())