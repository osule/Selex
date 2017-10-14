class HomePageController(object):
    def __init__(self, browser):
        self.browser = browser

    def visit_to_home_page(self):
        self.browser.get('http://benalman.com/about/')
    
    def read_title(self):
        elems = self.browser.find_elements_by_css_selector('#header-logo a')
        return elems[0].text

    def read_nav_links(self):
        link_selector = '.topnav ul li a'
        elems = self.browser.find_elements_by_css_selector(link_selector)
        return elems, link_selector
    
    def visit_nav_link(self, link_selector):
        elems = self.browser.find_elements_by_css_selector(link_selector)
        elems[0].click()
    
    def view_search(self):
        pass