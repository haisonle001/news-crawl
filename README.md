# News_Crawler
## Scrape articles from baomoi.com and related news



News crawler là tool được sử dụng để scrape các bài báo từ trang [baomoi.com](https://baomoi.com), từ các bài báo đó, công cụ sẽ tìm kiếm các bài báo khác có cùng nội dung, được xuất bản cùng một thời điểm và lưu vào kho dữ liệu.


## Chức năng

- Scrape links tất cả các bài báo mới nhất từ trang [baomoi.com](https://baomoi.com)
- Scrape và lưu articles từ links tìm được
- Search, scrape và lưu các bài báo có liên quan theo tiêu đề của các articles đã lưu



## Lưu 
> - Người dùng bắt buộc phải có một danh sách các proxy (sock5)  theo tài khoản để sử dụng tool.  (ex: https://dichvusocks.us/)
> 
> - Cài dặt các packages cần thiết trong requirements.txt bằng lệnh:
> ```sh
> pip install -r requirements.txt
> ```
> - Developer đã tuỳ chỉnh lại [**_\_\_init__.py_**](https://github.com/Nv7-GitHub/googlesearch/blob/master/googlesearch/__init__.py) thuộc package [googlesearch](https://github.com/Nv7-GitHub/googlesearch). Thay thế source code [**_\_\_init__.py_**](https://github.com/Nv7-GitHub/googlesearch/blob/master/googlesearch/__init__.py) bằng source code của [googlesreach_init_.py](googlesearch_init_.py)
>
> - Cần nhiều thời gian để tool thực thi xong công việc,  trung bình crawl nội dung 1 bài báo mất khoảng 1 giây, tuỳ thuộc  vào số lượng bài báo người dùng muốn crawl, có thể can thiệp vào source code để tuỳ chỉnh theo nhu cầu.


## Các bước sử dụng



- Khởi chạy [articles_crawler.py](Crawlers/articles_crawler.py) để crawl các bài báo mới nhất. 
Quá trình crawl được thể hiện trên console. 
- Lưu danh sách các proxy vào file [proxylist.txt](Crawlers/Proxies/proxylist.txt)
- Thay đổi **_username_** và **_password_** trong [testing_proxies.py](Crawlers/Proxies/testing_proxies.py) và [related_articles_crawler.py](Crawlers/related_articles_crawler.py) theo tài khoản socks của cá nhân người dùng
```sh
auth = HTTPProxyAuth("username", "password")
```
- Khởi chạy [testing_proxies.py](Crawlers/Proxies/testing_proxies.py) để test các proxy khả dụng và xoá đi các proxy không dùng được
- Khởi chạy [related_articles_crawler.py](Crawlers/related_articles_crawler.py) để tìm kiếm và crawl các bài báo có liên quan
- Kiểm tra và cập nhật [proxylist.txt](Crawlers/Proxies/proxylist.txt) thường xuyên 


