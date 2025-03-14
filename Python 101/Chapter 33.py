import requests

#r = requests.get('http://www.google.com/')
#print(dir(r))
#print(r.headers)

url = 'https://duckduckgo.com/html/'
payload = {'q':'python'}
r = requests.get(url, params=payload)
with open("requests_results.html","wb") as f:
    f.write(r.content)