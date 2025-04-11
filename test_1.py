import time

from selenium import webdriver


def test_browser():
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless--")
		driver = webdriver.Chrome(options=chrome_options)

		driver.get("https://cricbuzz.com")

		time.sleep(1)
