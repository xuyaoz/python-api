import urllib.request

response = urllib.request.urlopen('http://127.0.0.1:8868/xuyz?a=87&b=5')

html = response.read().decode("utf-8")
print(html)
