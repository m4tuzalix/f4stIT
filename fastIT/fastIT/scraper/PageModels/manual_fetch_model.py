from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from scraper.JavaScript.javascript import main_js, scroll_js
from time import sleep
from os import path

class ManualFetch():
    def __init__(self, link=None, all_links=None, city=None, bar_scroll=None, date_posted=None):
        """
        :param str: link -> selector:
        :param str: all_links -> selector:
        :param str: city -> selector:
        :param str: city_name -> selector:
        :param str: bar_scroll -> selector:
        :param str: date_posted -> selector:
        """
        self.all_links = all_links
        self.link = link
        self.city = city
        self.bar_scroll = bar_scroll
        self.date_posted = date_posted
        self.days = 1 #// adverts created within the given number
        self._timer = 700 #// scrolling pixels value
        self.links_array = []
        self.delay = 10
        print(f"Manual fetching started: {self.link}")
    
    def _open_web(self):
        """
        Creates selenium instance
        :return:
        """
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--enable-javascript")
        # self.options.add_argument("--headless")
        self.browser = webdriver.Chrome(path.abspath("chromedriver.exe"), chrome_options=self.options)
        self.browser.set_script_timeout(10)
        self.browser.implicitly_wait(self.delay)
        self.browser.maximize_window()
        self.browser.get(self.link)

    def _get_all_links(self):
        """
        returns list of all available job offers available within the page scope
        :return array:
        """
        return self.browser.find_elements(By.CSS_SELECTOR, self.all_links)
    
    def _get_position_name(self, link, position):
        """
        returns text for position's name selector
        :param str: link -> selector:
        :param str: position -> selector:
        :return string:
        """
        name = link.find_element(By.CSS_SELECTOR, position).text
        return name

    def _link_validation(self, link, position_selector, *args):
        """
        validates if contains valid city and is not older:higher (in terms of days) than int->self.days
        :param str: link -> selector:
        :param str: position_selector -> selector:
        :param args:
        :return bool:
        """
        link_href = link.find_element(By.TAG_NAME, "a").get_attribute("href")
        position_name = self._get_position_name(link, position_selector)
        if validation := self.browser.execute_script(main_js, self.days, self.city, link, self.date_posted):
            self.links_array.append((link_href, position_name))
            return True
        return False

    
    def _scroll_down(self):
        """
        Triggers js script responsible for scrolling(down) the page. int: self.timer, respresents pixels
        :return:
        """
        try:
            scrolling = self.browser.execute_script(scroll_js, self.bar_scroll, self._timer, self.link) #// Scrolling down triggers the divs to appear on the page
        except:
            return False

    def _close_web(self):
        """
        disconnects db and closes the browser
        :return:
        """
        self.browser.quit()