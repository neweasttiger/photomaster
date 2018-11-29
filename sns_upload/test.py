import facebook

def main():
   # Fill in the values noted in previous steps here
    cfg = {
    "page_id"      : "287793918534663",  # Step 1
    "access_token" : "EAAhMWuz15eEBAPCf9oMc4mZAsRJZBi4DqZC27JNteKoxoYcDWCtGXNwEo3aivuBmK4U96pSY5dg4MFmWLlPMmjxgI49oy68ZB308oZBEQ4ymCcEOHJAk1nnpdCuJOugniY3BwIeLidcZBHONXrmTEH6EaZCKEJXaFtenwQeqM8CkQphZC2l3eh2RonThXpquAZBNa1UrfpFmZAtwZDZD"   # Step 3
    }

    api = get_api(cfg)
    msg = "Hello, world!"
    status = api.put_wall_post(msg)

def get_api(cfg):
     graph = facebook.GraphAPI(cfg['EAAhMWuz15eEBAPCf9oMc4mZAsRJZBi4DqZC27JNteKoxoYcDWCtGXNwEo3aivuBmK4U96pSY5dg4MFmWLlPMmjxgI49oy68ZB308oZBEQ4ymCcEOHJAk1nnpdCuJOugniY3BwIeLidcZBHONXrmTEH6EaZCKEJXaFtenwQeqM8CkQphZC2l3eh2RonThXpquAZBNa1UrfpFmZAtwZDZD'])
     # Get page token to post as the page. You can skip 
     # the following if you want to post as yourself. 
     resp = graph.get_object('me/accounts')
     page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['287793918534663']:
            page_access_token = page['EAAhMWuz15eEBAPCf9oMc4mZAsRJZBi4DqZC27JNteKoxoYcDWCtGXNwEo3aivuBmK4U96pSY5dg4MFmWLlPMmjxgI49oy68ZB308oZBEQ4ymCcEOHJAk1nnpdCuJOugniY3BwIeLidcZBHONXrmTEH6EaZCKEJXaFtenwQeqM8CkQphZC2l3eh2RonThXpquAZBNa1UrfpFmZAtwZDZD']
    graph = facebook.GraphAPI(page_access_token)
    return graph

if __name__ == "__main__":
     main()
