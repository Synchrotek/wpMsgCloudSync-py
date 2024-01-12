from selenium import webdriver
import time

# Set the path to the Firefox browser executable
firefox_path = "geckodriver.exe"

# Set the path to the Firefox profile directory
profile_path = (
    "C:/Users/satya/AppData/Local/Mozilla/Firefox/Profiles/3m5744nz.default-release"
)

# Set the options for the Firefox browser
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("-profile")
firefox_options.add_argument(profile_path)

# Create a new instance of the Firefox browser with the specified profile
driver = webdriver.Firefox(options=firefox_options)

# Open Facebook.com
driver.get("https://www.facebook.com")
time.sleep(20)

# Close the browser
driver.quit()
