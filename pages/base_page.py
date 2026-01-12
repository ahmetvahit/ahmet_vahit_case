"""Base Page class with common methods for all page objects."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait[ChromeDriver](driver, 15)
    
    def navigate_to(self, url):
        """Navigate to specified URL."""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Find element with explicit wait."""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements with explicit wait."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def wait_for_element(self, locator):
        """Wait for element to be visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        """Click element after waiting for it to be clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def get_text(self, locator):
        """Get text content of element."""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible within timeout."""
        try:
            wait = WebDriverWait[ChromeDriver](self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Get current page URL."""
        return self.driver.current_url
    
    def scroll_to_element(self, locator):
        """Scroll to element."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def wait_for_page_load(self):
        """Wait for page to fully load."""
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    def switch_to_new_window(self):
        """Switch to newly opened window."""
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])
        self.wait_for_page_load()