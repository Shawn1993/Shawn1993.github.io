#!/usr/bin/env python
import urllib.request
import re

# 爬取种子链接源码
request = urllib.request.urlopen('https://www.zybuluo.com/ShawnNg/note/553404')
if request.getcode() != 200:
    print('Error code:' + request.getcode())
    exit()
source = request.read().decode('utf-8')

# 正则表达式提取信息
pattern = r'''<li class="file-item item" file-created-date="(.+?)T(.+?)Z">
\s*?<a tabindex="-1" href="(.+?)" title="【已发布】 (.+?)T(.+?)Z">
\s*?<i class="icon-share-sign"></i>
\s*?<span id=".+?">(.+?)</span>
\s*?</a>
\s*?</li>
'''
infos = re.compile(pattern).findall(source)

# 生成对应的post文档
content = '''---
date: {}
title: '{}'
categories: {}
tag: {}
---
<script language="javascript" type="text/javascript">
window.location.href = "{}"
</script>
'''
for cdate, ctime, link, udate, utime, title in infos:
    fname = '{}-{}.md'.format(cdate, title.replace(':', '_').replace('-', '_'))
    with open(fname, 'w') as file:
        file.write(content.format(cdate, title, '', '', link))
