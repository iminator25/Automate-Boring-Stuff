import schedule
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


	#Using Selenium 
print('Its starting...')

# setting the variables
url = 'https://www.facebook.com/'
my_user = 'imey25@hotmail.com'
my_pass = 'pass'

# starting the selenium driver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome()
driver.get(url)

# finding the elements from the login page and clicking submit
username = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')
submit = driver.find_element_by_id('loginbutton')
username.send_keys(my_user)
password.send_keys(my_pass)
submit.click()
time.sleep(3)

print('Logged In...')


# Open Birthdays 
bday_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/a')
bday_button.click()
print('Opened Birthdays')
time.sleep(4)

#send Birthday message:
msg = 'happy birthday'
bday_text = driver.find_element_by_class_name('a._8o _8s lfloat _ohe')
person = bday_text.get_attribute('title')
print('hereeeee',person)



# while True:
# 	schedule.run_pending()
# 	time.sleep(1)