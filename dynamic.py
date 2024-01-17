# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from collections import deque
import regex

# poopy = """잡히지
# 손
# 자신""".splitlines()

poopy = open("input.txt", encoding='utf8').read().splitlines()
q = deque()

for k in poopy:
    q.append(k)

while q:
    k = q.popleft()
    url = f"https://korean.dict.naver.com/koendict/#/search?query={k}&range=example"
    print(url)
    driver = webdriver.Firefox()# Open a web page

    # Create a request interceptor
    def interceptor(request):
        del request.headers['JSESSIONID']  # Delete the header first
        request.headers['JSESSIONID'] = '1051C2681B0DD90C396F809708F1F5A3'

    # Set the interceptor on the driver
    driver.request_interceptor = interceptor
    driver.get(url)

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "component_example"))
    )

    if element.text:
        lines = element.text.splitlines()
        n = len(lines)

        f = open(f"{k}.tsv", 'wb')
        f.write(b"KOREAN\tENGLISH\n")

        ind = 0
        while ind < n:
            if regex.search(r'\p{IsHangul}', lines[ind]):
                # print(lines[ind])
                write_string = lines[ind] + '\t' + lines[ind+1] + '\n'
                f.write(write_string.encode())
            ind += 1
    else:
        print("nopers")
        q.append(k)

    driver.quit()
