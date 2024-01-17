# pip install selenium
# pip install regex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import deque
import regex

# poopy = """잡히지
# 손
# 자신""".splitlines()


poopy = open("input.txt", encoding='utf8').read().splitlines()
q = deque()

f = open(f"korean.tsv", 'w', encoding='utf8')
f.write("word,ko1,en1,ko2,en2,ko3,en3,ko4,en4,ko5,en5\n")

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

        ans = ['' for _ in range(11)]
        ans[0] = k
        write_index = 1

        i = 1
        while i < n - 1:
            if regex.search(r'\p{IsHangul}', lines[i]) and not regex.search(r'\p{IsHangul}', lines[i+1]):
                if write_index > 10: break
                ans[write_index] = lines[i]
                ans[write_index+1] = '\"' + lines[i+1] + '\"'
                write_index += 2
            i += 1

        f.write(",".join(ans) + '\n')

    else:
        print("nopers")
        q.append(k)

    driver.quit()

f.close()