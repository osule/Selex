"""
 - test About page
 - check navigation links
 - check search

 - test Search page
 - check search box input
 - check search results
 - check pagination on search results
"""
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from controllers import (
    HomePageController,
    SearchPageController
)


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()


class HomePageTest(BaseTest):
    def setUp(self):
        homepage_controller = HomePageController(HomePageTest.browser)
        homepage_controller.visit_to_home_page()
        self.homepage_controller = homepage_controller

    def test_title_is_present_on_home_page(self):
        blog_author = self.homepage_controller.read_title()
        self.assertIn('BEN ALMAN', blog_author)

    def test_navigation_links(self):
        links, selector = self.homepage_controller.read_nav_links()
        self.assertEqual(len(links), 6)

        # for num, link in enumerate(links):
        #     links, selector = self.homepage_controller.read_nav_links()
        #     self.homepage_controller.visit_nav_link(selector + ":nth-child({})".format(num+1))

class SearchPageTest(BaseTest):
    def setUp(self):
        searchpage_controller = SearchPageController(SearchPageTest.browser)
        searchpage_controller.visit_home_page()
        self.searchpage_controller = searchpage_controller
    
    def test_make_query(self):
        self.searchpage_controller.make_query('Javascript')

        heading = self.searchpage_controller.view_text_in_query_result('#content_body0-inner')
        self.assertTrue(heading.startswith('SEARCH RESULTS'))

        results = self.searchpage_controller.view_query_results()
        self.assertIn('result', results)

if __name__ == "__main__":
    unittest.main()    

