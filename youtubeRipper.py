###       VVVVVVVVVVVVV

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#removes the excess time description and weird switch phrase based on whether or not sections split by a space has a colon
def clean(string):
    listsplit = string.split(" ")
    listsplit = (s for s in listsplit if not hasInvalidCharacter(s))
    return ' '.join(listsplit)

def hasInvalidCharacter(section):
    return ':' in section #or '-' in section

driver=webdriver.Firefox()


f = open('youtube_list.txt', 'r')
for line in f:

    baseurl = "http://youtube.com"
    driver.get("http://youtube.com")

    search = clean(line)
    print(search)

    firstnameField = driver.find_element_by_id("masthead-search-term")
    submitButton = driver.find_element_by_id("search-btn")

    firstnameField.send_keys(search)
    submitButton.click()

    linkclass = driver.find_element_by_css_selector('a.yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link ')
    print(linkclass.get_attribute("href"))

    #starting the conversion
    driver.get("http://www.youtube-mp3.org/")


#actions=ActionChanins(driver).click(firstnameField.send_key("T").lastnameField.send_keys("Gao").submitButton.click()
#actions.perform()

#print(driver.find_element_by_tag_name("body").text)
#driver.close()
