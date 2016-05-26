###       VVVVVVVVVVVVV

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import os

#removes the excess time description and weird switch phrase based on whether or not sections split by a space has a colon
def clean(string):
    string = string + '\n'
    listsplit = string.split(" ")
    listsplit = (s for s in listsplit if not hasInvalidCharacter(s))
    return ' '.join(listsplit)

def hasInvalidCharacter(section):
    return ':' in section #or '-' in section

#profile = webdriver.FirefoxProfile()
#profile.set_preference('browser.download.folderList', 2)
#profile.set_preference('browser.download.manager.showWhenStarting', False)
#profile.set_preference('browser.download.dir', os.getcwd())
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/vnd.ms-excel'))
#profile.set_preference("privacy.popups.disable_from_plugins", 3)
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(profile)

print('in order for this to work, you need to set firefox\'s download to automatic and the youtube list needs to have a newline at the end')

f = open('youtube_list.txt', 'r')
for line in f:

    driver.get("http://youtube.com")

    search = clean(line)
    print(search)

    firstnameField = driver.find_element_by_id("masthead-search-term")
    #submitButton = driver.find_element_by_id("search-btn")

    firstnameField.send_keys(search)
    #firstnameField.send_keys("hotel california")
    #submitButton.click()

    #linkclass = driver.find_element_by_class_name('yt-uix-tile-link')
    linkclass = driver.find_element_by_css_selector('.yt-uix-tile-link.spf-link')
    #print(linkclass.get_attribute("href"))
    url = linkclass.get_attribute("href")

    #starting the conversion
    #driver.get("http://www.youtube-mp3.org/")
    driver.get("http://www.onlinevideoconverter.com/mp3-converter")

    #inputs url and hits submit
    #youtube_url_field = driver.find_element_by_id('youtube-url')
    youtube_url_field = driver.find_element_by_css_selector('#texturl')
    youtube_url_field.clear()
    youtube_url_field.send_keys(url)
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('#convert1').click()

    #wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.presence_of_element_located((By.ID, "downloadq")))

    #driver.get(element.get_attribute('href'))
    #element.click()
    #driver.find_element_by_css_selector('#dl_link').click()
    driver.find_element_by_class_name('download-button').click()


#actions=ActionChanins(driver).click(firstnameField.send_key("T").lastnameField.send_keys("Gao").submitButton.click()
#actions.perform()

#print(driver.find_element_by_tag_name("body").text)
#driver.close()
