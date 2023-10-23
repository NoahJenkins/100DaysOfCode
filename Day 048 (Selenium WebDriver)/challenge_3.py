from selenium import webdriver 
from selenium.webdriver.common.by import By

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# Locate elements by appropriate strategy (e.g., By.NAME, By.ID, By.XPATH, etc.)
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# Input data
first_name.send_keys("Noah")
last_name.send_keys("Jenkins")
email.send_keys("email@email.com")

#Click Object
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()