from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

amazon_url = 'https://www.amazon.com/Portable-Mechanical-Keyboard-MageGee-Backlit/dp/B098LG3N6R/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.yn0LBKrl5MYB8Znoxfb--0CDf879L3qZ121v4MbU3_xme6Bkepdy3R4ATqtH8rFsgiCXk131or4jDoRk8Pn-k653OzB_Zqs6C1wE5X24esk7CO7KhaUL13T-UlVU8xcZ4LUKDePKlqHgBPMPPF2bJwxMSYT6Ur4AzWaw2MxgRjkOadjUNwEeOnK97Ym9_xduxt7xdN-DEEqYUubMjgVdY_rGJaWatGZEYYIvWgsgofE._yUivz4dVVt-CYNtA7wwkDemDv9rmaLFP0-pOv2YQsg&dib_tag=se&keywords=gaming+keyboard&pd_rd_r=28b63b94-2d4c-4f62-81cb-06a35c3db36c&pd_rd_w=lBrpo&pd_rd_wg=welNO&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=V1109FTJ013J8AGRHM1X&qid=1711708933&sr=8-1'

python_url = 'https://www.python.org'
wikipedia_main_page_url = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(options=chrome_options)
driver.get(wikipedia_main_page_url)

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# prince_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"The price is {price_dollar.text}.{prince_cents.text}")

# search_input = driver.find_element(By.NAME, value='field-keywords')

# print(search_input.tag_name)
# print(search_input.get_attribute('placeholder'))

# search_button = driver.find_element(By.ID, value='nav-search-submit-button')
# print(search_button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# connectivity_text = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[9]/div[3]/div[4]/div[41]/div/div[1]/div/table/tbody/tr[3]/td[1]/span')
# print(connectivity_text.text)

# event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

# for time in event_times:
#     print(time.text)

# for name in event_names:
#     print(name.text)

# events = { n: { 'time' : event_times[n].text, 'name': event_names[n].text} for n in range(len(event_times))}
# print(events)

# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()
# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, value='Reference desk')
# all_portals.click()

# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python', Keys.ENTER)

# driver.close() # closes tab
# driver.quit() # closes the browser