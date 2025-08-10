# Playwright scraping logic
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

CAPTCHA_URL = "https://csis.tshc.gov.in/"
CAPTCHA_PATH = "static/captcha.png"

def generate_captcha_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(CAPTCHA_URL)
        # page.screenshot(path=CAPTCHA_PATH)
        browser.close()

def fetch_case_data(case_type, case_number, case_year, captcha_text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(CAPTCHA_URL)

        page.select_option("select[name='caseType']", case_type)
        page.fill("input[name='caseNumber']", case_number)
        page.fill("input[name='caseYear']", case_year)
        page.fill("input[name='captcha']", captcha_text)
        page.click("input[type='submit']")
        page.wait_for_timeout(3000)

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    result = {}

    table = soup.find("table")
    if not table:
        result["error"] = "Invalid CAPTCHA or case not found."
        return result

    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            key = cols[0].get_text(strip=True)
            val = cols[1].get_text(strip=True)
            result[key] = val

    return result
