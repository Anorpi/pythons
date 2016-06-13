import requests
r = requests.get('https://github.com/timeline.json')
print r
rpost = requests.post("http://httpbin.org/post")
print rpost
rput = requests.put("http://httpbin.org/put")
print rput
rdelete = requests.delete("http://httpbin.org/delete")
print rdelete
rhead = requests.head("http://httpbin.org/get")
print rhead
ropt = requests.options("http://httpbin.org/get")
print ropt
