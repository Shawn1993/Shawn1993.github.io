#!/usr/bin/env python

import os
import sys


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

# read posts map
with open('posts_map.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        date, title, link = tuple(line.split(';'))
        fname = '{}-{}.md'.format(date, title.replace(':','_').replace('-','_'))
        with open(fname, 'w') as file:
            file.write(content.format(date, title, '', '', link))


