import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome("C:/chromedriver_win32 (1)/chromedriver.exe")
        driver.get("https://www.google.com")
        driver.maximize_window()
        search_box = driver.find_element_by_css_selector("input[title='Search']")
        search_box.send_keys("python tutorial")
        time.sleep(2)
        submit_button = driver.find_element_by_css_selector("input[value='Google Search']")
        submit_button.click()
        time.sleep(2)
        list = ["https://docs.python.org/3/tutorial/", "https://www.w3schools.com/python/",
                "https://www.tutorialspoint.com/python/index.htm", "https://www.learnpython.org/",
                "https://www.programiz.com/python-programming/tutorial", "https://www.programiz.com/python-programming",
                "https://www.guru99.com/python-tutorials.html", "https://www.javatpoint.com/python-tutorial",
                "https://realpython.com/"]

        for i in range(9):
            links = driver.find_elements_by_xpath("//div[@id='rso'] /div[@class='g'] /div /div //h3".replace('1', 'i'))
            linksDescription = driver.find_elements_by_xpath("//div[@id='rso'] /div[@class='g'] //div[@class='s']".replace('1', 'i'))
            actions = ActionChains(driver)
            actions.move_to_element(linksDescription[i]).perform()
            time.sleep(2)
            links[i].click()
            time.sleep(2)
            assert driver.current_url in list
            time.sleep(2)
            driver.back()
            time.sleep(2)
            i += 1
            time.sleep(2)
