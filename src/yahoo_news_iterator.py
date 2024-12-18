from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tqdm import tqdm

driver = webdriver.Chrome()

driver.get('https://finance.yahoo.com/quote/AAPL/news/')

articles_container = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ul.stream-items.yf-1usaaz9"))
)

i = 0
target_article_count = 50
ads = 0
valid_articles = 0

article_txt_data = []

while i < target_article_count:

    print(f'iteration {i}')

    # if i > 25:
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #must be reloaded every time you reload the homepage
    articles = driver.find_elements(By.CSS_SELECTOR, "ul.stream-items.yf-1usaaz9 > li")

    print('number of articles: ', len(articles))
    
    article = articles[i]
    article_class = article.get_attribute("class")

    if "ad-item" in article_class:
        ads += 1
        i += 1
        continue
    
    #scroll to target article
    driver.execute_script("arguments[0].scrollIntoView(false);", article)

    #wait for the target_article to become clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(article)
    )

    #click on the target article
    article.click()

    paragraph_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.body.yf-tsvcyu"))
    )

    #Go to the part of the page that conains the text
    driver.execute_script("arguments[0].scrollIntoView(true);", paragraph_container)

    # Wait for all paragraphs to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.yf-1pe5jgt"))
    )

    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.yf-1pe5jgt")

    article = ""

    for paragraph in paragraphs:
        article += paragraph.text.strip().replace("\"", "\'")

    i += 1
    valid_articles += 1

    article_txt_data.append(article)

    #return back to the previous page
    driver.back()

    time.sleep(0.5)

print(article_txt_data)
print("number of articles collectec: ", )

if input("Type 'quit' to finish session: ") == 'quit':
    driver.quit()