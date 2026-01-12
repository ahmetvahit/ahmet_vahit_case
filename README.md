# 📄 QA Engineer – Case Study Submission

## Overview

This repository contains an **end-to-end automated test case** prepared for the **Insider QA Engineer Assessment Project**.  
The test scenario validates the **Quality Assurance job listing flow** on the Insider website using **Python**, **Selenium**, and the **Page Object Model (POM)** approach.

---

## 🛠️ Tools & Technologies

| Technology | Description |
|------------|-------------|
| **Programming Language** | Python 3.8+ |
| **Test Framework** | `unittest` (Python's standard testing framework) |
| **Automation Tool** | Selenium WebDriver |
| **Design Pattern** | Page Object Model (POM) |
| **Driver Management** | webdriver-manager |
| **Browser** | Google Chrome (Chromium-based) |

> **Note:** The `unittest` framework was preferred as it is Python's **standard testing framework**, **non-BDD based**, and **fully compliant** with the given case requirements.

---

## 📋 Test Scenario Coverage

The automated test covers the following steps:

### ✅ Step 1: Home Page Validation
1. Navigate to `https://insiderone.com/`
2. Verify that the home page is opened successfully
3. Validate that all main page blocks (logo, navigation, footer, etc.) are loaded

### ✅ Step 2: Navigate to Quality Assurance Careers
1. Navigate to **Careers → Quality Assurance** page
2. Click **"See all QA jobs"** button
3. Verify that the jobs page is loaded correctly

### ✅ Step 3: Apply Filters on Jobs Page
1. Apply filters:
   - **Location:** Istanbul, Turkiye
   - **Department:** Quality Assurance
2. Verify that the job list is displayed

### ✅ Step 4: Validate Job Listings
Each listed job is validated to contain:
- **Position:** "Quality Assurance"
- **Department:** "Quality Assurance"
- **Location:** "Istanbul, Turkiye"

### ✅ Step 5: Verify Redirection to Lever
1. Click **"View Role"** button on the first job
2. Verify redirection to the **Lever Application Form** page

---

## ⚠️ Important Note on Location Value

In the case description, the location value is specified as **"Istanbul, Turkey"**.  
However, during implementation it was observed that:

- The HTML content and UI display the location as **"Istanbul, Turkiye"**
- Filtered job listings also use **"Istanbul, Turkiye"** instead of "Turkey"

**For this reason, assertions and validations are implemented based on the actual values rendered by the application**, ensuring **accurate and reliable test results**.

---

## 📁 Project Structure

```
ahmet_vahit_case/
├── pages/
│   ├── __init__.py
│   ├── base_page.py          # BasePage: Common WebDriver actions and wait mechanisms
│   ├── home_page.py           # HomePage: Home page locators and actions
│   ├── careers_page.py        # CareersPage: Careers QA page locators and actions
│   └── jobs_page.py           # JobsPage: Jobs listing, filtering, and validation
├── tests/
│   ├── __init__.py
│   └── test_insider_jobs.py   # Main test case with unittest framework
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### Architecture

- **BasePage:** Common WebDriver actions and wait mechanisms are centralized in `BasePage`
- **Page Objects:** Each page object encapsulates its own locators and behaviors
- **Test Class:** The test class focuses only on the test flow and assertions

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone <repository-url>
cd ahmet_vahit_case
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Chrome Browser
Ensure **Google Chrome** is installed on your system.  
ChromeDriver will be managed automatically by `webdriver-manager`.

---

## ▶️ How to Run the Test

### Method 1: Run with unittest module (Recommended)
```bash
python -m unittest tests.test_insider_jobs -v
```

### Method 2: Run directly
```bash
python tests/test_insider_jobs.py
```

### Expected Output
```
=== Test Step 1: Visiting Insider Home Page ===
[OK] Home page opened successfully
[OK] All main blocks are loaded

=== Test Step 2: Navigating to Careers Page ===
[OK] Careers page loaded successfully

=== Clicking 'See all QA jobs' button ===
[OK] Clicked 'See all QA jobs' button
[OK] Jobs page loaded successfully

=== Filtering jobs ===
[OK] Filtered by Location: Istanbul, Turkiye
[OK] Filtered by Department: Quality Assurance
[OK] Jobs list is present

=== Test Step 3: Verifying Job Details ===
[OK] All jobs contain 'Quality Assurance' in Position
[OK] All jobs contain 'Quality Assurance' in Department
[OK] All jobs contain 'Istanbul, Turkiye' in Location

=== Test Step 4: Clicking 'View Role' Button ===
[OK] Clicked 'View Role' button
[OK] Redirected to Lever Application form page

=== TEST COMPLETED SUCCESSFULLY ===
```

---

## 📝 Notes on Implementation

### ✅ Optimized Selectors
- **CSS selectors** are used instead of brittle absolute XPaths
- Selectors follow best practices for maintainability and performance

### ✅ Explicit Waits
- **Explicit waits** are preferred over implicit waits to improve test stability
- Custom wait conditions are implemented for dynamic content (e.g., filtering results)
- `WebDriverWait` is used with appropriate conditions (`visibility_of_element_located`, `presence_of_element_located`, etc.)

### ✅ Assertions at Every Step
- Assertions are applied at every critical step
- Test fails fast with clear error messages
- `unittest` assertions: `assertTrue()`, `assertEqual()`, etc.

### ✅ Code Quality
- Code readability and maintainability were prioritized
- Clear method names and comprehensive docstrings
- Follows **PEP 8** Python style guidelines
- No hardcoded waits (`time.sleep()`) – only explicit waits

### ✅ Page Object Model (POM)
- Each page has its own class with encapsulated locators and actions
- Reusable methods in `BasePage`
- Test code is separated from page logic

---

## 🧪 Test Case Details

### Home Page Verification
- **URL Check:** Validates the current URL contains `insiderone.com`
- **Element Check:** Logo, navigation menu, and footer are visible

### Careers Page Verification
- **URL Check:** Validates the current URL contains `careers/quality-assurance`
- **Element Check:** "See all QA jobs" button is visible and clickable
- **Title Check:** Page title contains "Quality Assurance"

### Jobs Page Verification
- **URL Check:** Validates the URL contains `careers/open-positions?department=qualityassurance`
- **Filter Check:** Location and Department filters are visible and functional
- **Job List Check:** Jobs are displayed after filtering
- **Dynamic Loading:** Waits for job items to be fully loaded before validation

### Job Validation Logic
- Iterates through all job listings
- Validates each job contains:
  - **Position:** "Quality Assurance"
  - **Department:** "Quality Assurance"
  - **Location:** "Istanbul, Turkiye"
- Reports any validation errors with detailed messages

### Lever Redirection Verification
- Clicks the "View Role" button on the first job
- Switches to the newly opened window
- Validates the URL contains `jobs.lever.co/insider`

---

## 🎯 Final Remarks

This case study was designed to reflect **real-world QA practices**, focusing on:

- ✅ **Reliability:** Explicit waits and stable locators ensure test consistency
- ✅ **Maintainability:** POM pattern allows easy updates when UI changes
- ✅ **Clear Validation Logic:** Comprehensive assertions with meaningful error messages
- ✅ **Accurate Handling of UI Edge Cases:** Handles actual rendered values (e.g., "Turkiye" vs "Turkey")
- ✅ **Professional Standards:** Clean code, proper documentation, and industry best practices

---

## 📧 Contact

**Ahmet Vahit TOPAN**  
Insider QA Engineer Case Study Submission

---

## 📜 License

This project was developed for assessment purposes.
