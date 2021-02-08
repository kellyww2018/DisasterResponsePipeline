import selenium
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

DRIVER_PATH = '/Users/yaxinwan/Desktop/AMF/neufluence-selenium/chromedriver'
LOGIN_URL = 'https://www.instagram.com/accounts/login'
BASE_URL = 'https://www.instagram.com'
USERNAME = 'biancarangle'
PASSWORD = 'Lfntihtmow745#5'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
print('got driver')

driver.get(LOGIN_URL)
print('login page')

driver.implicitly_wait(20)
login = driver.find_element_by_name('username').send_keys(USERNAME)
password = driver.find_element_by_name('password').send_keys(PASSWORD)
submit = driver.find_element_by_css_selector("button[type='submit']").click()
driver.implicitly_wait(10)
##submit = driver.find_element_by_css_selector("button[class='sqd0P.yWX7d.y3zKF']").click()
#driver.find_element_by_xpath(".//div[@class='cmbtv']//button[@class='sqd0P.yWX7d.y3zKF']").click()
driver.find_element_by_xpath('//button[text()="Not Now"]').click()
driver.implicitly_wait(10)
#driver.find_element_by_xpath('//button[text()="Not Now"]').click()
#driver.find_element_by_class_name('sqd0P yWX7d y3zKF').click()
#driver.implicitly_wait(10)
driver.find_element_by_link_text(USERNAME).click()
#driver.find_element_by_link_text("biancarangle's profile picture").click()
#driver.find_element_by_css_selector("//img[contains(@src, 'alt=biancarangle's profile picture')]").click()

print(driver.find_element_by_link_text(USERNAME))

print('after submit')

#driver.find_element_by_xpath('//a[contains(@href,"href")]')
#driver.find_element_by_xpath('//a[@href="/' + USERNAME + '/followers/"]').click()

# getting number of followers
#number_of_followers = driver.find_element_by_class_name('g47SY.lOXF2').get_attribute("title")
number_of_followers = int(driver.find_element_by_xpath("//li[contains(@class,'LH36I')]//a[contains(@class,'_81NM2')]//span[contains(@class,'g47SY lOXF2')]").get_attribute("title"))
print(number_of_followers)
driver.find_element_by_xpath('//a[@href="/' + USERNAME + '/followers/"]').click()

number_of_scrolls = 0

quotient, remainder = divmod(number_of_followers, 12)
number_of_scrolls = quotient + remainder

print(number_of_scrolls)


while number_of_scrolls > 0:
    time.sleep(1)
    driver.execute_script("document.querySelector('div.isgrP').scroll(0, 10000)")
    print("scroll")
    number_of_scrolls -= 1
    time.sleep(1)

#driver.execute_script("document.querySelector('div.isgrP').scroll(0, 10000)")


ul = driver.find_element_by_class_name('jSC57._6xe7A')
followers = ul.find_elements_by_tag_name("li")
last_username = ""

for follower in followers:
    url = follower.find_element_by_class_name('FPmhX.notranslate._0imsa').text
    print("url -> " + url)
    #username = follower.find_element_by_class_name('_7UhW9.xLCgt.MMzan._0PwGv.fDxYl').text
    username = follower.find_element_by_class_name('wFPL8').text
    print("username -> " + username)


print("")
print("")

print()


driver.close()
