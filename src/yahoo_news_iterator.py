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
article_count = 0
target_article_count = 25

print("initial article count: ", article_count)

while article_count < target_article_count:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    articles = driver.find_elements(By.CSS_SELECTOR, "ul.stream-items.yf-1usaaz9 > li")
    
    article_count = len(articles)
    i += 1
    print(f"article count after {i} th iteration: ", article_count)

valid_articles = 0
ads = 0

for article in tqdm(articles):

    article_class = article.get_attribute("class")

    #condition for if the article is an ad, skip it
    if "ad-item" in article_class:
        ads += 1
        continue

    valid_articles += 1

    

if input("Type 'quit' to finish session: ") == 'quit':
    driver.quit()