#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

with open('C:\\Users\\CNS\\Pictures\\98701_web.mp4', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata));