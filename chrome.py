from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time

# Specify the path to the geckodriver executable
service = Service(executable_path=r"geckodriver.exe")

# Configure Firefox options (if needed)
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")  # Uncomment this line if you want to run Firefox in headless mode

# Create a Firefox webdriver instance
driver = webdriver.Firefox(service=service, options=options)

# Open the desired website
driver.get("https://www.google.com/")

# Add any necessary waiting time or other interactions here if needed
# For example, waiting for an element to be present
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "some_element_id")))

# Close the browser after some time (for demonstration purposes)
time.sleep(10)
driver.quit()
