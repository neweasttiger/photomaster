# coding=utf-8
 
import facebook
 
graph = facebook.GraphAPI(access_token=[EAAhMWuz15eEBAPCf9oMc4mZAsRJZBi4DqZC27JNteKoxoYcDWCtGXNwEo3aivuBmK4U96pSY5dg4MFmWLlPMmjxgI49oy68ZB308oZBEQ4ymCcEOHJAk1nnpdCuJOugniY3BwIeLidcZBHONXrmTEH6EaZCKEJXaFtenwQeqM8CkQphZC2l3eh2RonThXpquAZBNa1UrfpFmZAtwZDZD], version="2.7")
 
site_info = graph.get_object(id="toypython", fields=["287793918534663","Embedded software test"])

print(site_info)
