from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://finance.yahoo.com/quote/AAPL/news/')

#checks whether the article exists in the paget
#target_article is a WebElement object that you are able to run a bunch of commands with
target_article = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h3.clamp.yf-18q3fnf"))
)

#scroll to target article
driver.execute_script("arguments[0].scrollIntoView(false);", target_article)

#wait for the target_article to become clickable
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(target_article)
)

#click on the target article
target_article.click()

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

print(article)

if input("Type 'quit' to finish session: ") == 'quit':
    driver.quit()
