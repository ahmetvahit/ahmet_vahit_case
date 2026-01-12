"""Home Page object for Insider website."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for Insider home page."""
    
    URL = "https://insiderone.com/"
    LOGO = (By.CSS_SELECTOR, "div.header-logo")
    NAVIGATION_HEADER = (By.CSS_SELECTOR, "header#navigation")
    HEADER_TOP_MENU = (By.CSS_SELECTOR, "div.header-top-menu")
    HEADER_TOP_ACTION = (By.CSS_SELECTOR, "div.header-top-action")
    FOOTER = (By.CSS_SELECTOR, "footer#footer")
    COOKIE_ACCEPT_BUTTON = (By.ID, "wt-cli-accept-all-btn")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Navigate to home page and accept cookies if present."""
        self.navigate_to(self.URL)
        self.wait_for_page_load()
        self.accept_cookies_if_present()
    
    def accept_cookies_if_present(self):
        """Accept cookie banner if it appears."""
        try:
            if self.is_element_visible(self.COOKIE_ACCEPT_BUTTON, timeout=3):
                self.click_element(self.COOKIE_ACCEPT_BUTTON)
        except:
            pass
    
    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO)
    
    def is_navigation_menu_visible(self):
        return self.is_element_visible(self.NAVIGATION_HEADER)
    
    def is_header_top_menu_visible(self):
        return self.is_element_visible(self.HEADER_TOP_MENU)
    
    def is_header_top_action_visible(self):
        return self.is_element_visible(self.HEADER_TOP_ACTION)
    
    def is_footer_visible(self):
        return self.is_element_visible(self.FOOTER)
    
    def are_main_blocks_loaded(self):
        """Check if all main page blocks are loaded and visible."""
        return (self.is_logo_visible() and 
                self.is_navigation_menu_visible() and 
                self.is_header_top_menu_visible() and
                self.is_header_top_action_visible() and
                self.is_footer_visible())
    
    def is_page_loaded(self):
        """Verify page is fully loaded with correct URL and elements."""
        current_url = self.get_current_url()
        url_check = current_url.rstrip("/") == "https://insiderone.com"
        elements_loaded = self.are_main_blocks_loaded()
        return url_check and elements_loaded
    
    def verify_home_page_opened(self):
        """Verify home page opened successfully."""
        return self.is_page_loaded()
