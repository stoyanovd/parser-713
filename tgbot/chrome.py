import os

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options


# buildpacks for Heroku:
# https://github.com/heroku/heroku-buildpack-chromedriver

# normal mode
# https://github.com/heroku/heroku-buildpack-xvfb-google-chrome

# headless mode
# https://github.com/heroku/heroku-buildpack-google-chrome

def get_chrome():
    chrome_options = Options()
    chrome_options.binary_location = os.environ['GOOGLE_CHROME_BIN']
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.WebDriver(executable_path=os.environ['CHROMEDRIVER_PATH'],
                                 chrome_options=chrome_options)

    return driver
