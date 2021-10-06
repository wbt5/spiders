# -*- coding: utf-8 -*-
# @Time: 2021/10/7 0:02
# @Project: my-spiders
# @Author: wbt5
# @Blog: https://wbt5.com
import base64
import random
import time

import requests


def get_analysis(params, url):
    i = '00000008d78d46a'
    f = -(random.randint(100, 10000))
    o = int(time.time() * 1000) - (f or 0) - 1515125653845
    r = base64.b64encode(params.encode()).decode()
    r = f'{r}@#{url}@#{o}@#1'
    e = len(r)
    n = len(i)
    ne = ''
    for _ in range(0, e):
        ne += chr(ord(r[_]) ^ ord(i[(_ + 10) % n]))
    ne = base64.b64encode(ne.encode()).decode()
    return ne


def get_comment():
    baseurl = 'https://api.qimai.cn'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 Safari/537.36',
        'referer': 'https://www.qimai.cn/',
        # 'cookies': cookies,
    }
    url = '/app/comment'
    params = {
        'sword': '',
        'edate': '2021-10-04 23:59:59',
        'sdate': '2021-09-05 00:00:00',
        'appid': 414478124,
        'country': 'cn',
    }
    data = ''.join(sorted([str(v) for v in params.values()]))
    analysis = get_analysis(data, url)
    params['analysis'] = analysis

    res = requests.get(f'{baseurl}{url}', params=params, headers=headers).json()
    if res['msg'] == '成功':
        items = res['appComments']
        return items
    else:
        pass
