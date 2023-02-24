import sys
import ast
import json
import random

import requests
from googlesearch import search
from newsplease import NewsPlease
# auth for proxy
from requests.auth import HTTPProxyAuth
from underthesea import ner


print('Related articles crawler is running...')

auth = HTTPProxyAuth("nductai1792", "Taiprovodoi113")

# init proxy list
proxy_list = []
for line in open("Proxies/proxylist.txt", "r"):
    line = line[:-1]
    proxy_list.append(line)

# init User agents list
User_agents_list = []
for line in open("Proxies/user-agents.txt", "r"):
    # line=line[:-1]
    t_line = ast.literal_eval(line)
    User_agents_list.append(t_line)


with open("result/articles_baomoi.txt", "r",encoding='utf8') as fp:
    num_articles = sum(1 for line in fp)


# open files for extract and save data
fi = open("result/articles_baomoi.txt", "r",encoding='utf8')


fo = open("result/related_articles.txt", 'w',encoding='utf8')

# --------------------------
count_proxy = -1


# get next proxy from proxies list
def next_proxy():
    url = "http://ipinfo.io/json"
    global count_proxy
    while (True):
        count_proxy += 1
        if (count_proxy == len(proxy_list)): count_proxy = 0
        proxy = proxy_list[count_proxy]

        # check proxy
        try:
            response = requests.get(url, proxies={"http": "socks5://" + str(proxy), "https": "socks5://" + str(proxy)},
                                    auth=auth, timeout=1)
            return (proxy)
            break
        except:
            pass


# get random User Agent
def random_UAs():
    i = random.randint(0, len(User_agents_list) - 1)
    return(User_agents_list[i])


count=0

def print_progress():
    global count
    count += 1
    i = count
    sys.stdout.write(f"\rFinding news related to article: %i/{num_articles}" % i)
    sys.stdout.flush()


for line in fi.readlines():
    # analyze title and date
    a = json.loads(line)
    t_str = ner(a["title"])
    t_date = (a["date"])
    searching_key = a["title"]

    # source init
    source = [line]

    # Change proxy
    proxy = next_proxy()
    usr_agent = random_UAs()
    print_progress()
    print('\n','++++++++++++++++++++++++')
    # Crawl Links from googlesearch
    links = search(searching_key, lang="vn",
                   proxies={"http": "socks5://" + str(proxy), "https": "socks5://" + str(proxy)}, usr_agent=usr_agent,
                   auth=auth, num_results=5)
    print('------------------------')
    for link in links:
        print(link)
        try:    
            article = NewsPlease.from_url(link)  # article check!
            if (article.date_publish != None) & (str(article.date_publish.date()) == t_date[:-9]):
                if (article.title != None) & (article.description != None) & (article.maintext != None):
                    news = {'title': article.title, 'description': article.description, 'content': article.maintext,
                            'date': str(article.date_publish)}
                    source.append(news)
                else: break

        except Exception as E:
            pass

    fo.write(json.dumps(source, ensure_ascii=False))
    fo.write('\n')

print("Done!")
