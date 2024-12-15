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

#Get the first paragraph of the article
#wait for the element to become available
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located("div.body-wrap.yf-i23rhs")
)

#Scroll to the section of the page with the article, may not be necessary
# content = driver.find_element(By.CLASS_NAME, "body-wrap")
# ActionChains(driver).scroll_to_element(content).perform()

if input("Type 'quit' to finish session: ") == 'quit':
    driver.quit()