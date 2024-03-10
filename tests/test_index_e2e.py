import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ENETests(unittest.TestCase):

    def setUp(self) -> None:
        # Set up Chrome options
        options = webdriver.ChromeOptions()

        # Initialize the Chrome WebDriver with ChromeOptions
        self.driver = webdriver.Chrome(options=options)

        # Navigate to the specified URL
        self.driver.get("http://localhost:5000")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn("Named Entity", self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading")
        self.assertEqual("Named Entity Header", heading.text)

    def test_page_has_input_for_text(self):
        input_element = self._find("input-text")
        self.assertIsNotNone(input_element)

    def test_page_has_a_button_for_submitting_text(self):
        submit_button = self._find("find-button")
        self.assertIsNotNone(submit_button)

    def test_submitting_sentence_creates_a_table(self):
        input_element = self._find("input-text")
        submit_button = self._find("find-button")
        input_element.send_keys("France and Germany share a border in Europe")
        submit_button.click()
        table = self._find("ner-table")
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, f"[data-test-id='{val}']")