from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# option - keep the browser opn (helps diagnose if the script crashes)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

# Get cookie to click on
cookie = driver.find_elements(By.ID, value='cookie')

# get upgrade items ids
items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
item_ids = [item.get_attribute('id') for item in items]

timeout = time.time() * 5 # 5 seconds
five_min = time.time() + 60 * 5  # 5 minutes

while True:
  cookie.click()

  # every 5 seconds
  if time.time() > timeout:


      # get all upgrade <b> tags
      all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
      item_prices = []

      # convert <b> text into a interger price
      for price in all_prices:
        element_text = price.text
        if element_text != '':
          cost = int(element_text.split('-')[1].strip().replace(',',''))
          item_prices.append(cost)

      # create dictionary of store items and prices
      cookie_upgrades = {}
      for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

      # get current cookie count
      money_element = driver.find_elemenmt(By.ID, value='money').text
      if ',' in money_element:
        money_element = money_element.replace(',', '')
      cookie_count = int(money_element)
      
      # find upgrades that we can currently afford
      affordable_upgrades = {}
      for cost, id in cookie_upgrades.items():
        if cookie_count > cost:
          affordable_upgrades[cost] = id

      # purchase the most expensive affordable upgrade
      highest_price_affordable_upgrade = max(affordable_upgrades)
      print(highest_price_affordable_upgrade)
      to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

      driver.find_element(By.ID, value=to_purchase_id). click()

      # add another 5 seconds until the next check
      timeout = time.time() * 5

  # after 5 minutes stop the bot and check the cookies per second count
  if time.time() > five_min:
    cookie_per_s = driver.find_element(By.ID, value='cps').text
    print(cookie_per_s)
    break

  
