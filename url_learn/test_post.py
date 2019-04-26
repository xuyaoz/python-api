import urllib.request
import urllib.parse

url = 'http://127.0.0.1:8832/post'
values = {"a": 43,
          "b": 32}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)

