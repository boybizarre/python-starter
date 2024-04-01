from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_UP = 150
PROMISED_DOWN = 10
TWITTER_EMAIL = 'johndoe_'
TWITTER_PASSWORD = ''



class InternetSpeedTwitterBot: 
    def __init__(self, driver_path):
      self.chrome_options = webdriver.ChromeOptions().add_experimental_option('detach', True)
      self.driver_path = driver_path
      self.driver = webdriver.Chrome(options=self.chrome_options)
      self.up = 0
      self.down = 0

    def get_internet_speed(self):
      self.driver.get(self.driver_path)

      time.sleep(10)
      # click continue button (privacy)
      continue_button = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
      continue_button.click()

      # click GO button
      go_button = self.driver.find_element(By.CLASS_NAME, value='start-text')
      go_button.click()

      # wait 60 seconds
      time.sleep(60)

      self.up = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[3]/span')
      self.down = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[4]/span')
      

    def tweet_at_provider(self):
      self.driver.get("https://twitter.com")

      time.sleep(5)
      # click on sign in button
      sign_in_button = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')

      time.sleep(10)
      email = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
      email.send_keys(Keys.ENTER)

      time.sleep(10)
      password = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
      password.send_keys(Keys.ENTER)

      time.sleep(10)
      tweet_compose = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span/span')

      tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
      tweet_compose.send_keys(tweet)

      post = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
      post.click()

      time.sleep(2)
      self.driver.quit()




bot = InternetSpeedTwitterBot('https://www.speedtest.net/')
bot.get_internet_speed()
bot.tweet_at_provider()
