from bs4 import BeautifulSoup
import urllib.request
import requests 

inp = "잡히지"

cookies = {'JSESSIONID': 'DCB686E0BDE6DCD698EBCC3633A35DCB'}

r = requests.post('https://korean.dict.naver.com/koendict/#/search?query=%EC%9E%A1%ED%9E%88%EC%A7%80&range=example', cookies=cookies)

print(r.text)


# for search_term in inp:
#     # url = urllib.request.urlopen('https://korean.dict.naver.com/koendict/#/search?query={search_term}EC%A7%80&range=example')
#     response = requests.get('https://korean.dict.naver.com/koendict/#/search?query=%EC%9E%A1%ED%9E%88%EC%A7%80&range=example') 
#     html = response.text 
#     print(html)

    # print(BeautifulSoup(page, 'html.parser').prettify(), file=open('lol', 'w'))
    # soup = BeautifulSoup(page, 'html.parser')
    # print(soup)
    # mydivs = soup.find_all("div", {"class": "component_example has-saving-function"}
    # print(mydivs)
    # search for class component_example has-saving-function