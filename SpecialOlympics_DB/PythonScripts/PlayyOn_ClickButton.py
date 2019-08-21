
from selenium import webdriver
from chromedriver import main

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.playyon.com/admin/people/')

# click radio button
python_button = driver.find_elements_by_xpath("//*[@id='people']/div/div[1]/div[1]/label")[0]
python_button.click()


