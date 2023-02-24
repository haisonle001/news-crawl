import json
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from newsplease import NewsPlease


def print_progress(func, end):
    global count
    count += 1
    i = count
    sys.stdout.write(f"\r{func}: %i{end}" % i)
    sys.stdout.flush()


def scraping_link(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'lxml')

    for links in soup.findAll('h4'):

        for a in links.findAll('a', href=True):
            f.write(urljoin(base, a['href']))
            f.write('\n')
        print_progress('Links crawled: ', '')


# --------------------Links crawler-----------------------
base = 'https://baomoi.com/'
f = open("result/links_baomoi.txt", "w")
categories = ['the-gioi', 'thoi-su', 'giao-thong', 'moi-truong-khi-hau', 'nghe-thuat', 'am-thuc', 'du-lich',
              'lao-dong-viec-lam', 'tai-chinh', 'chung-khoan', 'kinh-doanh', 'hoc-bong-du-hoc', 'dao-tao-thi-cu',
              'bong-da-quoc-te','bong-da-viet-nam', 'quan-vot', 'am-nhac', 'thoi-trang', 'dien-anh-truyen-hinh',
              'an-ninh-trat-tu', 'hinh-su-dan-su', 'cntt-vien-thong', 'thiet-bi-phan-cung', 'khoa-hoc',
              'dinh-duong-lam-dep', 'tinh-yeu-hon-nhan', 'suc-khoe-y-te', 'xe-co', 'quan-ly-quy-hoach',
              'khong-gian-kien-truc']

count = 0
print('Links crawler from https://baomoi.com is running...')

for i in range(1, 168):
    for category in categories:
        scraping_link("https://baomoi.com/" + category + "/trang" + str(i) + ".epi")
    if i == 1: break

print("\nDone!")
f.close()

# ------------------------Articles crawler-----------------------------
fi = open("result/links_baomoi.txt", "r")
fo = open("result/articles_baomoi.txt", "w")
print("Articles crawler from https://baomoi.com is running...")

news = {}
link_count = count
count = 0
for line in fi.readlines():
    link = line.strip()
    while (True):
        article = NewsPlease.from_url(link, timeout=5)
        if article.maintext == None: break
        t_title = article.title
        t_description = article.description
        t_content = article.maintext
        t_date = str(article.date_publish)
        news = {'title': t_title, 'description': t_description, 'content': t_content, 'date': t_date}
        fo.write(json.dumps(news, ensure_ascii=False))
        fo.write('\n')
        print_progress("Articles crawled: ", f'/{link_count}')
        break

print("\nDone")
fi.close()
fo.close()
