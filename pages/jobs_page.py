"""Jobs Page object with filtering and job listing operations."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from pages.base_page import BasePage


class JobsPage(BasePage):
    """Page object for Insider jobs listing page."""
    
    LOCATION_FILTER = (By.CSS_SELECTOR, "select#filter-by-location")
    DEPARTMENT_FILTER = (By.CSS_SELECTOR, "select#filter-by-department")
    JOB_ITEMS = (By.CSS_SELECTOR, "div.position-list-item")
    JOB_POSITION_TITLE = (By.CSS_SELECTOR, "p.position-title")
    JOB_DEPARTMENT = (By.CSS_SELECTOR, "span.position-department")
    JOB_LOCATION = (By.CSS_SELECTOR, "div.position-location")
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, "a.btn")
    LEVER_APPLY_BUTTON = (By.CSS_SELECTOR, "a.postings-btn")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_page_loaded(self):
        """Verify jobs page is fully loaded with filters."""
        current_url = self.get_current_url()
        url_check = ("careers/open-positions" in current_url and 
                     "department=qualityassurance" in current_url)
        location_filter_visible = self.is_element_visible(self.LOCATION_FILTER)
        department_filter_visible = self.is_element_visible(self.DEPARTMENT_FILTER)
        return url_check and location_filter_visible and department_filter_visible
    
    def wait_for_jobs_to_load(self):
        """Wait for job listings to load."""
        try:
            self.wait.until(EC.presence_of_element_located(self.JOB_ITEMS))
        except:
            pass
        self.wait_for_page_load()
    
    def wait_for_jobs_filtered_by_location(self, expected_location):
        """Wait until all jobs are filtered by expected location."""
        def all_jobs_have_expected_location(driver):
            try:
                jobs = driver.find_elements(*self.JOB_ITEMS)
                if len(jobs) == 0:
                    return False
                for job in jobs:
                    location_element = WebDriverWait[ChromeDriver](job, 20).until(
                        EC.presence_of_element_located(self.JOB_LOCATION)
                    )
                    if expected_location not in location_element.text:
                        return False
                return True
            except:
                return False
        self.wait.until(all_jobs_have_expected_location)
    
    def filter_by_location(self, location):
        """Filter jobs by location."""
        if not self.is_page_loaded():
            raise Exception("Jobs page is not loaded properly")
        
        self.wait_for_jobs_to_load()
        location_dropdown = self.find_element(self.LOCATION_FILTER)
        select = Select(location_dropdown)
        location_class = location.replace(" ", "").replace(",", "").lower()
        
        try:
            option = location_dropdown.find_element(By.CSS_SELECTOR, f"option.job-location.{location_class}")
            select.select_by_visible_text(option.text)
        except:
            try:
                select.select_by_visible_text(location)
            except:
                location_alt = location.replace("Turkey", "Turkiye")
                select.select_by_visible_text(location_alt)
        
        self.wait_for_jobs_filtered_by_location(location)
    
    def filter_by_department(self, department):
        """Filter jobs by department."""
        department_dropdown = self.find_element(self.DEPARTMENT_FILTER)
        select = Select(department_dropdown)
        department_class = department.replace(" ", "").lower()
        
        try:
            option = department_dropdown.find_element(By.CSS_SELECTOR, f"option.job-team.{department_class}")
            select.select_by_visible_text(option.text)
        except:
            select.select_by_visible_text(department)
        
        self.wait_for_jobs_to_load()
    
    def get_all_job_items(self):
        """Get all job listing elements."""
        return self.driver.find_elements(*self.JOB_ITEMS)
    
    def is_job_list_present(self):
        """Check if job listings are present."""
        return len(self.get_all_job_items()) > 0
    
    def get_job_position(self, job_element):
        """Extract position title from job element."""
        return job_element.find_element(*self.JOB_POSITION_TITLE).text
    
    def get_job_department(self, job_element):
        """Extract department from job element."""
        return job_element.find_element(*self.JOB_DEPARTMENT).text
    
    def get_job_location(self, job_element):
        """Extract location from job element."""
        return job_element.find_element(*self.JOB_LOCATION).text
    
    def verify_all_jobs_contain(self, expected_position, expected_department, expected_location):
        """Verify all jobs contain expected criteria."""
        jobs = self.get_all_job_items()
        errors = []
        
        for index, job in enumerate(jobs, 1):
            position = self.get_job_position(job)
            department = self.get_job_department(job)
            location = self.get_job_location(job)
            
            if expected_position not in position:
                errors.append(f"Job {index}: Position '{position}' does not contain '{expected_position}'")
            if expected_department not in department:
                errors.append(f"Job {index}: Department '{department}' does not contain '{expected_department}'")
            if expected_location not in location:
                errors.append(f"Job {index}: Location '{location}' does not contain '{expected_location}'")
        
        return len(errors) == 0, errors
    
    def click_view_role_button(self, job_index=0):
        """Click 'View Role' button on specified job."""
        jobs = self.get_all_job_items()
        if job_index < len(jobs):
            job = jobs[job_index]
            view_role_btn = job.find_element(*self.VIEW_ROLE_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", view_role_btn)
            view_role_btn.click()
        else:
            raise IndexError(f"Job index {job_index} out of range")
    
    def is_redirected_to_lever(self):
        """Verify redirect to Lever application form."""
        self.switch_to_new_window()
        current_url = self.get_current_url()
        is_lever_url = "jobs.lever.co" in current_url
        is_apply_button_visible = self.is_element_visible(self.LEVER_APPLY_BUTTON, timeout=5)
        return is_lever_url and is_apply_button_visible
