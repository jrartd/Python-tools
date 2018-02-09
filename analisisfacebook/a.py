from urllib import urlopen, Request
url = "http://www.krugercorporation.com/"
request = Request(url)
response = urlopen(request)
html = response.read()
reponse.close()