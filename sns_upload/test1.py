# -*- coding: utf-8 -*- 

import facebook

graph = facebook.GraphAPI('EAAhMWuz15eEBALhY62pfBDm6MwML5spfG29EfIGbSJsD63RfWvCz2LvbUPq2fD7KsVT2lR44pxZBXuOEmV4DBaiauliCPjQ9zecBWxsALUrta8zpZCCqR8k6XKHPFqPFyCv0YCDNlI0hEvjPAU5XyhPZCd2ZAxuRZCfZCWrvEWTuBhO0vjlO4wQIirMNUeaUCYjG611adrgwZDZD')
graph.put_object("287793918534663", "feed", message='포스팅하고자하는 말')
