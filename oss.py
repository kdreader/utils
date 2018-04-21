# encoding: utf8

import re


def parse_oss_url(url):
    pattern = re.compile(r'(http|https)://([a-zA-Z0-9_-]+)\.(.*?)\/(.*)')
    match = pattern.match(url)
    if match:
        return match.groups()
    else:
        raise Exception('Invalid OSS url')
