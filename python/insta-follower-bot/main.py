from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.execptions import ElementClickInterceptedException

import time

SIMILAR_ACCOUNT = ''
USERNAME = 'spaceship_recordz'
PASSWORD = 'Ireayomide1'

class InstaFollower:
    def __init__(self, driver_path):
      self.chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True)
      self.driver_path = driver_path
      self.driver = webdriver.Chrome(options=self.chrome_options)


    def login(self):
      url = 'https://www.instagram.com/accounts/login/'
      self.driver.get(url)
      time.sleep(4.2)

      # Check if the cookie warning is present on the page
      decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
      cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)

      if cookie_warning:
        # Dismiss the cookie warning by clicking an element or button
        cookie_warning[0].click()

      username = self.driver.find_element(By.NAME, value='username')
      password = self.driver.find_element(By.NAME, value='password')

      username.send_keys(USERNAME)
      password.send_keys(PASSWORD)

      time.sleep(2.1)
      password.send_keys(Keys.ENTER)

      time.sleep(4.3)
      # click not now and ignore save login info prompt
      save_login_prompt = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")

      if save_login_prompt:
        save_login_prompt.click()
      
      time.sleep(3.7)

      # click not now for notifications prompt
      notifications_prompt = self.driver.find_element(By.XPATH, value="// button[contains(text(), 'Not Now')]")
      if notifications_prompt:
        notifications_prompt.click()

    def find_followers(self):
      time.sleep(5)

      # show followers of the selected account
      self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers')

      time.sleep(5.2)
      # The xpath of the modal that shows the followers will change over time. Update accordingly.
      modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
      modal = self.driver.find_element(By.XPATH, value=modal_xpath)

      for i in range(10):
        # In this case we're executing some Javascript, that's what the execute_script() method does.
        # The method can accept the script as well as an HTML element.
        # The modal in this case, becomes the arguments[0] in the script.
        # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)


    def follow(self):
      # check and update the (CSS) selector for the follow buttons as required
      all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='.__aano button')

      for button in all_buttons:
        try:
          button.click()
          time.sleep(2.1)
        # Clicking button for someone who is already being followed will trigger dialog to un-follow/Cancel
        except ElementClickInterceptedException:
          cancel_button = self.driver.find_elemnet(by-By.XPATH, value="//button[contains(text(), 'Cancel')]")
          cancel_button.click()


insta_bot = InstaFollower()

insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()