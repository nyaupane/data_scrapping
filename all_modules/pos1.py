import requests
r = requests.post("http://httpbin.org/post")
r.content
print r.content
