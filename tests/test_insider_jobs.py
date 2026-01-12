"""
Insider QA Jobs Test Case
Test Case Requirements:
1. Visit https://insiderone.com/ and check home page is opened and all main blocks are loaded
2. Go to https://insiderone.com/careers/quality-assurance/, click "See all QA jobs", 
   filter jobs by Location - Istanbul, Turkey and department - Quality Assurance, 
   check presence of jobs list
3. Check that all jobs' Position contains "Quality Assurance", Department contains "Quality Assurance", 
   Location contains "Istanbul, Turkey"
4. Click "View Role" button and check that this action redirects us to Lever Application form page
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage


class TestInsiderQAJobs(unittest.TestCase):
    """Test case for Insider QA job listings using Page Object Model."""
    
    @classmethod
    def setUpClass(cls):
        """Set up Chrome WebDriver with options."""
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
    
    def setUp(self):
        """Initialize page objects."""
        self.home_page = HomePage(self.driver)
        self.careers_page = CareersPage(self.driver)
        self.jobs_page = JobsPage(self.driver)
    
    def test_insider_jobs_flow(self):
        """Test complete flow from home page to job application."""
        print("\n=== Test Step 1: Visiting Insider Home Page ===")
        self.home_page.open()
        
        self.assertTrue(
            self.home_page.verify_home_page_opened(),
            "Home page URL should contain 'insiderone.com'"
        )
        print("[OK] Home page opened successfully")
        
        self.assertTrue(
            self.home_page.are_main_blocks_loaded(),
            "All main blocks (logo, navigation, footer) should be visible"
        )
        print("[OK] All main blocks are loaded")
        
        print("\n=== Test Step 2: Navigating to Careers Page ===")
        self.careers_page.open()
        
        self.assertTrue(
            self.careers_page.is_page_loaded(),
            "Careers page should be loaded"
        )
        print("[OK] Careers page loaded successfully")
        
        print("\n=== Clicking 'See all QA jobs' button ===")
        self.careers_page.click_see_all_qa_jobs()
        print("[OK] Clicked 'See all QA jobs' button")
        
        self.assertTrue(
            self.jobs_page.is_page_loaded(),
            "Jobs page should be loaded with filters visible"
        )
        print("[OK] Jobs page loaded successfully")
        
        print("\n=== Filtering jobs ===")
        self.jobs_page.filter_by_location("Istanbul, Turkiye")
        print("[OK] Filtered by Location: Istanbul, Turkiye")
        
        self.jobs_page.filter_by_department("Quality Assurance")
        print("[OK] Filtered by Department: Quality Assurance")
        
        self.assertTrue(
            self.jobs_page.is_job_list_present(),
            "Jobs list should be present after filtering"
        )
        print("[OK] Jobs list is present")
        
        print("\n=== Test Step 3: Verifying Job Details ===")
        all_valid, errors = self.jobs_page.verify_all_jobs_contain(
            expected_position="Quality Assurance",
            expected_department="Quality Assurance",
            expected_location="Istanbul, Turkiye"
        )
        
        if errors:
            print(f"\n[WARNING] Found {len(errors)} validation error(s):")
            for error in errors:
                print(f"  - {error}")
        
        self.assertTrue(
            all_valid,
            f"All jobs should contain expected values. Errors: {errors}"
        )
        print("[OK] All jobs contain 'Quality Assurance' in Position")
        print("[OK] All jobs contain 'Quality Assurance' in Department")
        print("[OK] All jobs contain 'Istanbul, Turkiye' in Location")
        
        print("\n=== Test Step 4: Clicking 'View Role' Button ===")
        self.jobs_page.click_view_role_button(job_index=0)
        print("[OK] Clicked 'View Role' button")
        
        self.assertTrue(
            self.jobs_page.is_redirected_to_lever(),
            "Should be redirected to Lever Application form page"
        )
        print("[OK] Redirected to Lever Application form page")
        
        print("\n=== TEST COMPLETED SUCCESSFULLY ===")
    
    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests."""
        if cls.driver:
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)