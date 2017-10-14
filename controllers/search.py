from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SearchPageController(object):
    def __init__(self, browser):
        self.browser = browser

    def visit_home_page(self):
        self.browser.get('http://benalman.com/about/')

    def make_query(self, query):
        search_box = self.browser.find_element_by_id('search')
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
        selector = '.gsc-result-info-container .gsc-result-info'
        wait = WebDriverWait(self.browser, 10)
        elems = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )

    def view_text_in_query_result(self, selector):
        elems = self.browser.find_element_by_css_selector(selector)
        return elems.text

    def view_query_results(self):
        selector = '.gsc-result-info-container .gsc-result-info'
        return self.view_text_in_query_result(selector)
    
    def view_next_result_page(self):
        pass
