# -*- coding: utf-8 -*- 

import facebook
import sys
import os


path = open('../path.txt',mode='rt')
patha=path.read()
pathb=patha.splitlines()[0]
pathc=patha.splitlines()[1]

r = open('../../{0}/log.txt'.format(pathb), mode='rt')
s=r.read()
photob=s.splitlines()[0]

print pathb
print pathc
print photob

graph = facebook.GraphAPI('EAAhMWuz15eEBAAPplvHKjudw0tQhWQASiEx8FHPZAEWTt2F7ECRZAp2A4mSkOaSZAnLIZAEjIghFIR5wQv1R0MixHDT97oC70ZBQGZCEbsbKJPe760Gt4ZA52FZAsMIOZAYMoxjZA6RFGZBuXiRDna4wwWnUo0QTQXJdOhYWwB2Pd9cQ5E9WJg5cMACuQq2TNu1vcnY36TH7ZAF97gZDZD')
graph.put_photo(image=open('../../{0}/{1}'.format(pathb,photob), 'rb'),
                message='{0}'.format(pathc))

path.close()
r.close()

