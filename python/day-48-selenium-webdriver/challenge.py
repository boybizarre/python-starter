from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

challenge_url = 'http://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Chrome(options=chrome_options)
driver.get(challenge_url)

# select name field
first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys('dev')
last_name.send_keys('python')
email.send_keys('python@gmail.com', Keys.ENTER)
