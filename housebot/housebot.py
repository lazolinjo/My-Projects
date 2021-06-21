from bs4 import BeautifulSoup
from requests import get



headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

url1 = "https://www.nekretnine.rs/"
response = get(url1, headers=headers)

print(response.text[:1000])