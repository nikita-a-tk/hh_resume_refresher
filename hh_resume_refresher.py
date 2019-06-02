# login to hh.ru
# click refresh resume date button
# import requests
import getpass
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

print('Enter your email:')
email = input()
print('Enter your password:')
password = getpass.getpass()

opts = Options()
opts.set_headless()
assert opts.headless

browser = Chrome(executable_path = './chromedriver')

browser.get('https://hh.ru/account/login')

username_field = browser.find_elements_by_xpath("//input[@type='email'][@data-qa='login-input-username']")[0]
password_field = browser.find_elements_by_xpath("//input[@type='password'][@data-qa='login-input-password']")[0]

username_field.send_keys(email)
password_field.send_keys(password)

login_button = browser.find_element_by_xpath("//input[@type='submit'][@data-qa='account-login-submit']")
login_button.click()

#tech support resume page
browser.get('https://hh.ru/resume/5561aee0ff0707ee8a0039ed1f45624c514372')
refresh_button = browser.find_element_by_xpath("//button[@data-qa='resume-update-button']")
refresh_button.click()

browser.close()
# quit()
