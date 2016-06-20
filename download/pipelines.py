# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
from urlparse import urlparse

baseDir = 'd:/downloads/autoDownloads'


class DownloadPipeline(object):
    def process_item(self, item, spider):
        host, file_dir, name = url_analyse(urlparse(item['src']))
        resp = requests.get(item['src'], stream=True)
        file_path = os.path.join(baseDir, host, file_dir)
        create_path(file_path)
        with open(os.path.join(file_path,name ), 'wb') as fd:
            for chunk in resp.iter_content():
                fd.write(chunk)

        return item


def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def url_analyse(url):
    i = len(url.path) - 1
    while i > 0:
        if url.path[i] == '/':
            break
        i = i - 1
    return url.hostname, url.path[1:i], url.path[i + 1:len(url.path)]
