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

graph = facebook.GraphAPI('EAAhMWuz15eEBAAIhBZBA5KRaYfZCfn9YV1yPoTZAelPibHrCYZB56uQnto8idHdbhZCMj92oZBaN76gZAZBSIVE39E6AHPZBdYxI0oZCGbcpobi9BK1BQ8AmnX2chBxm8R5evwr76gnoKJcDkIoWBFh4U0yc3qXiBrH8Ea0Cqxu5g5UpKChs7GZA95a6gfW1CmohexvaaJZCZCLrGZAAZDZD')
graph.put_photo(image=open('./{0}/{1}'.format(pathb,photob), 'rb'),
                message='{0}'.format(pathc))

path.close()
r.close()

