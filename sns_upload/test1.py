# -*- coding: utf-8 -*- 

import facebook

graph = facebook.GraphAPI('EAAhMWuz15eEBALhY62pfBDm6MwML5spfG29EfIGbSJsD63RfWvCz2LvbUPq2fD7KsVT2lR44pxZBXuOEmV4DBaiauliCPjQ9zecBWxsALUrta8zpZCCqR8k6XKHPFqPFyCv0YCDNlI0hEvjPAU5XyhPZCd2ZAxuRZCfZCWrvEWTuBhO0vjlO4wQIirMNUeaUCYjG611adrgwZDZD')
...
graph.put_object("287793918534663", "feed", message='사진포스트')

graph = facebook.GraphAPI(oauth_access_token)
...
photo = open("picture.jpg", "rb")
graph.put_object("287793918534663", "photos", message="You can put a caption here", source=photo.read())
photo.close()
