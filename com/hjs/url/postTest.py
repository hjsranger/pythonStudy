import urllib.parse
import urllib.request
import urllib.error
import socket


#带参数
data = bytes(urllib.parse.urlencode(({'hello':'world'})), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data = data)

print(response.read())

#timeout





try:
    responseForTimeout = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("都是时间惹的祸")



