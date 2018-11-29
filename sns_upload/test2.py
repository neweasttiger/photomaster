# -*- coding: utf-8 -*- 

import facebook

graph = facebook.GraphAPI('EAAhMWuz15eEBALhY62pfBDm6MwML5spfG29EfIGbSJsD63RfWvCz2LvbUPq2fD7KsVT2lR44pxZBXuOEmV4DBaiauliCPjQ9zecBWxsALUrta8zpZCCqR8k6XKHPFqPFyCv0YCDNlI0hEvjPAU5XyhPZCd2ZAxuRZCfZCWrvEWTuBhO0vjlO4wQIirMNUeaUCYjG611adrgwZDZD')
photo = open("picture.jpg", "rb")
#graph.put_object("287793918534663", "photos", message="You can put a caption here", source=photo.read())


# Upload an image with a caption.
graph.put_photo(image=open('picture.jpg', 'rb'),
                message='Look at this cool photo!')

photo.close()
