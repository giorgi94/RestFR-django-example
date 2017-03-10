# RestFR-django-example
---
This is a simple django project using REST framework.

By python module "requests" can be sent json data, for example:

    import requests
    auth=(email, password)
    data = {'text':'my comment'}
    link = 'http://localhost:8000/api/post/2/comment/'
    requests.post(link,auth=auth, json=data)
