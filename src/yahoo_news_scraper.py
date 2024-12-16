import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://finance.yahoo.com/quote/AAPL/news/')

#locates the first article
first_article = driver.find_element(By.CSS_SELECTOR, "h3.clamp.yf-18q3fnf")

#scrolls to the element
ActionChains(driver).scroll_to_element(first_article).perform()

#click on the element
first_article.click()

#Go to the part of the page that conains the text
paragraph_container = driver.find_element(By.CSS_SELECTOR, "div.body.yf-tsvcyu")
driver.execute_script("arguments[0].scrollIntoView(true);", paragraph_container)

# Wait for all paragraphs to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.yf-1pe5jgt"))
)

paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.yf-1pe5jgt")

for paragraph in paragraphs:
    print(paragraph.text)

if input("Type 'quit' to finish session: ") == 'quit':
    driver.quit()
