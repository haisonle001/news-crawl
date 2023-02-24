import requests
from requests.auth import HTTPProxyAuth

url = "http://ipinfo.io/json"
proxy_list = []
for line in open("proxylist.txt", "r"):
    line = line[:-1]
    proxy_list.append(line)

print(proxy_list)

auth = HTTPProxyAuth("nductai1792", "Taiprovodoi113")
f = open("proxylist.txt", "w")

i = -1
while (i < len(proxy_list) - 1):
    i += 1
    print("Request Number : " + str(i))
    proxy = proxy_list[i]
    print(proxy)
    try:
        response = requests.get(url, proxies={"http": "socks5://" + proxy, "https": "socks5://" + proxy}, auth=auth,
                                timeout=10)
        print("true")
        f.writelines(proxy + "\n")

    except:
        # if the proxy Ip is preoccupied
        print("false")
