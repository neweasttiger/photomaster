# -*- coding: utf-8 -*- 

import facebook

graph = facebook.GraphAPI('EAAhMWuz15eEBAOafZAQq9WFpjrrVz9B77vMV3gdafLZAtQoaXvyRo099ZBuV3btiulYZCKzC3DZCNKJJJ1Q2W6ZAWM7OVay3ZCSZBT7quwzqRJo645fUxKoya9cHcWmep7kGE9Tu4AzSmpZBX5K5ICHG73MIfZAdcPET8uzAV7mWWTCEk2UrdGDkzgSoHV6EIffrZCOINceRfZAbfAZDZD')
photo = open("picture.jpg", "rb")
#graph.put_object("287793918534663", "photos", message="You can put a caption here", source=photo.read())


# Upload an image with a caption.
graph.put_photo(image=open('picture.jpg', 'rb'),
                message='Look at this cool photo!')

photo.close()
