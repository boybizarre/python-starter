from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = 'johndoe@gmail.com'
ACCOUNT_PASSWORD = '{/password}/}'

LINKEDIN_URL ='https://www.linkedin.com/jobs/search/?currentJobId=3878295350&f_LF=f_AL&geoId=102257491&keywords=fullstack%20developer&location=London%2C%20England%2C%20United%20Kingdom'

def abort_application():
   # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

#  optional - to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)

# driver.get(
#     "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
#     "&keywords=fullstack%20developer"
#     "&location=London%2C%20England%2C%20United%20Kingdom"
#     "&redirect=false&position=1&pageNum=0"
# )

driver.get(LINKEDIN_URL)

# click reject cookies button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# click sign in button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value='Sign in')
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value='username')
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(by=By.ID, value='password')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
# input("Press Enter when you have solved the Captcha")

# click all the jobs
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container")

# APPLY for jobs
for listing in all_listings:
  print('Opening listing')
  listing.click()
  time.sleep(5)
  try:
    # locate the apply button
    time.sleep(10)
    apply_button = driver.find_element(By.CLASS_NAME, value='jobs-apply-button')
    apply_button.click()

    # next button email and phone number populated
    time.sleep(5)
    phone_submit = driver.find_element(By.CSS_SELECTOR, value='footer div button')
    if phone_submit.get_attribute("data-artdeco-is-focused") == "true":
        abort_application()
        print("Complex application, skipped.")
        continue
    else:
        # Click Submit Button
        print("Submitting phone number")
        phone_submit.click()

    # CV:Resume populated
    time.sleep(5)
    resume_submit = driver.find_element(By.CSS_SELECTOR, value='footer div button')
    if resume_submit.get_attribute("data-artdeco-is-focused") == "true":
        abort_application()
        print("Complex application, skipped.")
        continue
    else:
        # Click Submit Button
        print("Submitting CV:Resume")
        resume_submit.click()

    # click on review button
    time.sleep(5)
    review = driver.find_element(By.CSS_SELECTOR, value='footer div button')
    if review.get_attribute("data-artdeco-is-focused") == "true":
        abort_application()
        print("Complex application, skipped.")
        continue
    else:
        # Click Submit Button
        print("Clicking Review Button")
        review.click()
    
    # click on submit application button
    time.sleep(5)
    submit_application = driver.find_element(By.ID, value='ember617')
    if submit_application.get_attribute("data-artdeco-is-focused") == "true":
        abort_application()
        print("Complex application, skipped.")
        continue
    else:
        # Click Submit Button
        print("Clicking Review Button")
        submit_application.click()

  except NoSuchElementException:
    abort_application()
    print('Not application button, skipped')
    continue

time.sleep(5)
driver.quit()

print('DONE!')

'Review your application'
'Continue to next step'

