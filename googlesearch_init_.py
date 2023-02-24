from bs4 import BeautifulSoup
from requests import get
import random



def _req(term, results, lang, start, proxies, usr_agent, auth):
    resp = get(
        url="https://www.google.com/search",
        headers=usr_agent,
        params=dict(
            q=term,
            num=results + 2,  # Prevents multiple requests
            hl=lang,
            start=start,
        ),
        proxies=proxies,
        auth=auth
    )
    resp.raise_for_status()
    return resp

class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"

def search(term, num_results=10, lang="en", proxies=None, usr_agent=None, advanced=False, auth=None ,sleep_interval=0):
    escaped_term = term.replace(' ', '+')

    # Fetch
    start = 0
    while start < num_results:
        # Send request
        resp = _req(escaped_term, num_results-start, lang, start, proxies, usr_agent, auth)
        soup = BeautifulSoup(resp.text, 'lxml')
        result_block = soup.findAll('div', attrs={'class': 'yuRUbf'})
        if (len(result_block)==0): break
        for result in result_block:
            # Find link
            link = result.find('a', href=True)
            if link:
                start+=1
                yield link['href']
