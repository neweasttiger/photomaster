# -*- coding: utf-8 -*- 

import facebook
import sys
import os


path = open('./ILOVEAPPLE/path.txt',mode='rt')
patha=path.read()
pathb=patha.splitlines()[0]
pathc=patha.splitlines()[1]

r = open('./{0}/log.txt'.format(pathb), mode='rt')
s=r.read()
photob=s.splitlines()[0]

graph = facebook.GraphAPI('EAAhMWuz15eEBAPhZB0q5A8FMnQTXxoZAl79rZAHdlgBNtReYYDlzOSH7wKVzm4WV2LGv5M1Qf6pKbrcRthZB6aNgmZBK0UmZA06WpEJiRx7QUUtOk1lHmZCbdDxdiJTpLrVTZBPpru4cyQ7BRZCMKhRoWe89EzqqvgPcLvJimGhiFuFz2R05C1ThwTmWQfy6l0CY0pce5RcseYQZDZD')
graph.put_photo(image=open('./{0}/{1}'.format(pathb,photob), 'rb'),
                message='{0}'.format(pathc))

path.close()
r.close()

