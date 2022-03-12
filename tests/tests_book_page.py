from books import models
from tests.webdriver_test_case import WebdriverTestCase


class BookPageTests(WebdriverTestCase):
    '''Selenium tests for book page.'''

    def setUp(self):
        super().setUp()
        self.book = models.Book.objects.filter(title='1984').first()

    def _get_book_url(self) -> str:
        return f'{self.live_server_url}/books/{self.book.slug}'

    def _check_person_present_and_clickable(self,
                                            person: models.Person) -> None:
        self.driver.get(self._get_book_url())
        elem = self.driver.find_element_by_link_text(person.name)
        self.scroll_into_view(elem)
        elem.click()
        self.assertIn(f'/person/{person.slug}', self.driver.current_url)

    def test_click_authors(self):
        self.assertGreaterEqual(self.book.authors.count(), 1)
        for author in self.book.authors.all():
            self._check_person_present_and_clickable(author)

    def test_click_translators(self):
        self.assertGreaterEqual(self.book.translators.count(), 1)
        for translator in self.book.translators.all():
            self._check_person_present_and_clickable(translator)

    def test_click_narrators(self):
        self.assertGreaterEqual(self.book.narrations.count(), 1)
        for narration in self.book.narrations.all():
            for narrator in narration.narrators.all():
                self._check_person_present_and_clickable(narrator)

    def test_has_narration_links(self):
        self.assertGreaterEqual(self.book.narrations.count(), 1)
        self.driver.get(self._get_book_url())
        for narration in self.book.narrations.all():
            for link in narration.links.all():
                caption = link.url_type.caption
                elem = self.driver.find_element_by_link_text(caption)
                self.assertIsNotNone(elem)
                self.assertEqual(link.url, elem.get_dom_attribute('href'))

    def test_click_tags(self):
        self.assertGreaterEqual(self.book.tag.count(), 1)
        for tag in self.book.tag.all():
            self.driver.get(self._get_book_url())
            elem = self.driver.find_element_by_link_text(tag.name)
            self.scroll_into_view(elem)
            elem.click()
            self.assertIn(f'/books?books={tag.slug}', self.driver.current_url)
            tag_header = self.driver.find_element_by_css_selector(
                '#books .tag')
            self.assertEqual(tag.name, tag_header.text)

    def test_renders_text_elements(self):
        self.driver.get(self._get_book_url())
        book_elem = self.driver.find_element_by_css_selector('#books')
        self.assertIn('14 гадзін 15 хвілін', book_elem.text)
        self.assertEqual(f'{self.book.title} аўдыякніга', self.driver.title)
        description = self.driver.find_element_by_css_selector(
            'meta[name="description"]').get_dom_attribute('content')
        self.assertIn(self.book.title, description)
        self.assertIn(self.book.authors.first().name, description)