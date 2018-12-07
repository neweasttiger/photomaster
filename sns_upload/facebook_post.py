# -*- coding: utf-8 -*- 

import facebook
import sys
import os


r = open('/home/hongle/sweng-2018/coproject/photomaster/wildlife/picture.txt', mode='rt')
s=r.read()

print s.splitlines()[0]
graph = facebook.GraphAPI('EAAhMWuz15eEBADoMzNS96n4KxN1Fh0OMwinCjkDmQFeqnEiFFpQtdtZAsdp211NZCVJRhpbEloAgZAzh8WDArnjXZBESwdxRCMSZAAyUzkKJmPhnDgWvDythw40SlELhC6MiXBO7ZBa53FuQYUPZBzYFAUoTa4d2eNBpVBlNJDZCALHelHupgXr2lwd2QH6MihcHG8BFemuiNQZDZD')

graph.put_photo(image=open(s.splitlines()[0], 'rb'),
                message='Look at this cool photo!')


r.close()

