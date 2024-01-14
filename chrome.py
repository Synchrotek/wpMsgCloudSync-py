from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# custom_chrome_Binary = "chromedriver.exe"
# chrome_options.binary_location = custom_chrome_Binary


def verify_title():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://pypi.org/project/webdriver-manager/")

    title = driver.title
    expected_title = "webdriver-manager · PyPI"
    if title == expected_title:
        print("Title verification succesful!")
    else:
        print(f"Title verification failed\nExpected: {expected_title}, got: {title}")

    driver.quit()


def create_chrome_driver(profile_user_data):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--remote-debugging-port=8989")
    profile_path = f"user-data-dir={profile_user_data}"
    print(profile_path)
    chrome_options.add_argument(profile_path)
    chrome_options.add_argument('profile-directory="Test-Go"')
    # chrome_options.add_argument("--no-sandbox")

    print(chrome_options)

    driver = webdriver.Chrome(
        options=chrome_options,
        service=ChromeService(ChromeDriverManager().install()),
    )

    driver.get("https://web.whatsapp.com/")
    time.sleep(105)
    driver.quit()


if __name__ == "__main__":
    # Set the path to the user data directory
    profile_user_data = "C:/Users/satya/AppData/Local/Google/Chrome/User Data/Profile 1"
    create_chrome_driver(profile_user_data)
