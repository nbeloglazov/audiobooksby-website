import time
import unittest
from books import models
from tests.webdriver_test_case import WebdriverTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class HeaderAndSearchTests(WebdriverTestCase):
    '''Selenium tests for header elements including search.'''

    def get_first_book(self) -> models.Book:
        return models.Book.objects.filter(title='Ордэн белай мышы').first()

    def test_click_logo_leads_to_main_page(self):
        self.driver.get(f'{self.live_server_url}/books')
        self.driver.find_element_by_css_selector('.navbar .logo').click()
        self.assertEqual(f'{self.live_server_url}/', self.driver.current_url)

    @unittest.skip('waiting for navbar final shape')
    def test_click_site_title_to_main_page(self):
        self.driver.get(f'{self.live_server_url}/books')
        self.driver.find_element_by_css_selector('.navbar .site-title').click()
        self.assertEqual(f'{self.live_server_url}/', self.driver.current_url)

    def test_click_catalog(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('.navbar .catalog').click()
        self.assertEqual(f'{self.live_server_url}/books',
                         self.driver.current_url)

    def test_click_about_us(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('.navbar .about-us').click()
        self.assertEqual(f'{self.live_server_url}/about',
                         self.driver.current_url)

    def _wait_for_suggestion(self, text: str, link: str) -> None:
        autocomplete = self.driver.find_element_by_css_selector(
            '#autocomplete')
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            lambda wd: autocomplete.find_element(by=By.LINK_TEXT, value=text),
            f'Did not see suggestion with text "{text}"')
        self.assertEqual(link, element.get_dom_attribute('href'))

    def _init_algolia(self) -> None:
        self.driver.get(f'{self.live_server_url}/push_data_to_algolia')

    def test_client_side_search_book(self):
        self._init_algolia()
        self.driver.get(self.live_server_url)
        search = self.driver.find_element_by_css_selector('#search')
        for query in ['людзі', 'ЛЮДИ', 'ЛюДзИ']:
            search.clear()
            search.send_keys(query)
            self._wait_for_suggestion('Людзі на балоцеІ. Мележ',
                                      '/books/liudzi-na-balotse')

    def test_client_side_search_author(self):
        self._init_algolia()
        self.driver.get(self.live_server_url)
        search = self.driver.find_element_by_css_selector('#search')
        for query in ['каратк', 'КОРОТ']:
            search.clear()
            search.send_keys(query)
            self._wait_for_suggestion('Уладзімір Караткевіч',
                                      '/person/uladzimir-karatkevich')
