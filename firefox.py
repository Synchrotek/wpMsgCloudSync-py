from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.service import Service
import time


def create_firefox_driver(profile_path):
    firefox_exe = "geckodriver.exe"
    firefox_binary = "C:/Program Files/Mozilla Firefox/firefox.exe"
    firefox_options = Options()

    firefox_profile = FirefoxProfile(profile_path)
    firefox_options.profile = firefox_profile

    # firefox_options.add_argument("-profile")
    # firefox_options.add_argument(profile_path)

    # firefox_options.binary_location(firefox_binary)
    serv = Service(firefox_binary)
    driver = webdriver.Firefox(service=serv, options=firefox_options)
    print("Firefox opened")
    return driver


# Set the path to the Firefox profile directory
profile_path = "C:/Users/satya/AppData/Local/Mozilla/Firefox/Profiles/a9l3p7mh.testGo"

driver = create_firefox_driver(profile_path)

# Open Facebook.com
print("Started")
time.sleep(4)
driver.get("https://web.whatsapp.com/")
time.sleep(10)
print("Finsihed")

# Close the browser
driver.quit()
