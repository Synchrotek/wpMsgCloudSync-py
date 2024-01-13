from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=r"./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:/Users/satya/AppData/Local/Google/Chrome/User Data/"
)
options.add_argument("--profile-directory=Default")
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com/")
time.sleep(22)

# chat_name = "Name of the chat"
# chat_xpath = f"//span[@title='{chat_name}']"
# chat = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, chat_xpath))
# )
# chat.click()


# Media retrival -------------------------------------------------------
# media_xpath = "//div[contains(@class, 'message-in')]//div[contains(@class, 'media-thumb-container')]"
# media_elements = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.XPATH, media_xpath))
# )

# for media_element in media_elements:
#     media_element.click()
#     media_url = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@class='download']//a"))
#     )
#     media_url = media_url.get_attribute("href")
#     print(media_url)
