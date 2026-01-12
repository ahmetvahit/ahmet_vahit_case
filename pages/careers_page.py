"""Careers Page object for Insider Quality Assurance page."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    """Page object for Insider careers/quality-assurance page."""
    
    URL = "https://insiderone.com/careers/quality-assurance/"
    QA_TITLE = (By.CSS_SELECTOR, "h1.big-title")
    SEE_ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR, "a[href*='department=qualityassurance']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Navigate to Quality Assurance careers page."""
        self.navigate_to(self.URL)
        self.wait_for_page_load()
    
    def click_see_all_qa_jobs(self):
        """Click 'See all QA jobs' button."""
        self.scroll_to_element(self.SEE_ALL_QA_JOBS_BUTTON)
        self.click_element(self.SEE_ALL_QA_JOBS_BUTTON)
        self.wait_for_page_load()
    
    def is_on_qa_page(self):
        """Check if current page is Quality Assurance page."""
        element = self.wait_for_element(self.QA_TITLE)
        return element.text.strip() == "Quality Assurance"
    
    def is_page_loaded(self):
        """Verify careers page is fully loaded with correct elements."""
        current_url = self.get_current_url()
        url_check = "careers/quality-assurance" in current_url
        title_text_check = self.is_on_qa_page()
        
        if not self.is_element_visible(self.SEE_ALL_QA_JOBS_BUTTON):
            return False
        
        button_element = self.wait_for_element(self.SEE_ALL_QA_JOBS_BUTTON)
        button_text_check = button_element.text.strip() == "See all QA jobs"
        
        return url_check and title_text_check and button_text_check
