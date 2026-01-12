# QA Engineer – Case Study Submission

[![CI/CD Pipeline](https://github.com/ahmetvahit/ahmet_vahit_case/actions/workflows/ci.yml/badge.svg)](https://github.com/ahmetvahit/ahmet_vahit_case/actions)

## Overview

This repository contains an **end-to-end automated test case** prepared for the **Insider QA Engineer Assessment Project**.  
The test scenario validates the **Quality Assurance job listing flow** on the Insider website using **Python**, **Selenium**, and the **Page Object Model (POM)** approach.

---

## Tools & Technologies

| Technology | Description |
|------------|-------------|
| **Programming Language** | Python 3.8+ |
| **Test Framework** | `unittest` (Python's standard testing framework) |
| **Automation Tool** | Selenium WebDriver |
| **Design Pattern** | Page Object Model (POM) |
| **Driver Management** | webdriver-manager |
| **Browser** | Google Chrome (Chromium-based) |
| **CI/CD** | GitHub Actions |

> **Note:** The `unittest` framework was preferred as it is Python's **standard testing framework**, **non-BDD based**, and **fully compliant** with the given case requirements.

---

## Test Scenario Coverage

The automated test covers the following steps:

### Step 1: Home Page Validation
1. Navigate to `https://insiderone.com/`
2. Verify that the home page is opened successfully
3. Validate that all main page blocks (logo, navigation, footer, etc.) are loaded

### Step 2: Navigate to Quality Assurance Careers
1. Navigate to **Careers → Quality Assurance** page
2. Click **"See all QA jobs"** button
3. Verify that the jobs page is loaded correctly

### Step 3: Apply Filters on Jobs Page
1. Apply filters:
   - **Location:** Istanbul, Turkiye
   - **Department:** Quality Assurance
2. Verify that the job list is displayed

### Step 4: Validate Job Listings
Each listed job is validated to contain:
- **Position:** "Quality Assurance"
- **Department:** "Quality Assurance"
- **Location:** "Istanbul, Turkiye"

### Step 5: Verify Redirection to Lever
1. Click **"View Role"** button on the first job
2. Verify redirection to the **Lever Application Form** page

---

## Important Note

The case description specifies **"Istanbul, Turkey"**, but the application renders **"Istanbul, Turkiye"** in both UI and filtered results. Test assertions use the actual rendered value to ensure accuracy.

---

## Project Structure

```
ahmet_vahit_case/
├── pages/
│   ├── __init__.py
│   ├── base_page.py           # BasePage: Common WebDriver actions and wait mechanisms
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

## Installation & Setup

### 1. Prerequisites

**Python 3.8+ Required** (Tested with Python 3.13.7)

Check if Python is installed:
```bash
python --version
# or
python3 --version
```

If Python is not installed, download and install it:

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

**macOS:**
```bash
brew install python@3.13
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Clone the Repository
```bash
git clone https://github.com/ahmetvahit/ahmet_vahit_case.git
```

### 3. Create Virtual Environment   
```bash
python -m venv .venv
# or
python3 -m venv .venv
```

### 4. Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 5. Upgrade pip
```bash
python -m pip install --upgrade pip
```
### 6. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 7. Chrome Browser
Ensure **Google Chrome** is installed on your system.  
ChromeDriver will be managed automatically by `webdriver-manager`.

---

## Continuous Integration

This project includes a **GitHub Actions CI/CD pipeline** that automatically:
- Runs tests on every push and pull request
- Validates code in a clean Ubuntu environment with Chrome
- Generates test execution reports
- Displays test execution summary in the GitHub Actions tab (requires GitHub login to view)
- Provides test artifacts for download (requires GitHub login to view)

The pipeline status is shown by the badge at the top of this README.

---

## How to Run the Test

> **Note:** Make sure your virtual environment is activated before running tests.

### Run with unittest module
```bash
python -m unittest tests.test_insider_jobs -v
# or
python3 -m unittest tests.test_insider_jobs -v
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

## Test Implementation Highlights

- **Page Object Model (POM):** Each page has its own class with encapsulated locators and methods
- **Explicit Waits:** `WebDriverWait` (30s timeout) with appropriate conditions for dynamic content handling
- **Optimized Selectors:** CSS selectors prioritized for maintainability and performance
- **Comprehensive Validation:** URL checks, element visibility, filter functionality, and job listing criteria
- **Error Reporting:** Detailed validation messages with clear assertion points
- **No Hardcoded Delays:** Only explicit waits, no `time.sleep()` calls

---
## Contact

**Ahmet Vahit TOPAN**  
QA Engineer Case Study Submission

---

## License

This project was developed for assessment purposes.
