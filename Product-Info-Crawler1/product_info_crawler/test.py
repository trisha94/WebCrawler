import requests

proxies = {
  "http": "http://127.0.0.1:8118"
}

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11'
}

r = requests.get("http://www.telize.com/ip", proxies=proxies, headers=headers)

print (r.text)