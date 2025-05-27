from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import csv

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://owasp.org/www-project-top-ten/")

# wait element
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//li[a/strong]"))
)

results = []

items = driver.find_elements(By.XPATH, "//li[a/strong]")

for li in items:
    try:
        a_tag = li.find_element(By.TAG_NAME, "a")
        title = a_tag.find_element(By.TAG_NAME, "strong").text.strip()
        link = a_tag.get_attribute("href")
        full_text = li.text.strip()
        description = full_text.replace(title, "").strip()
        results.append({"Title": title, "Link": link, "Description": description})
        print(f"[+] {title}")
    except Exception as e:
        print(f"[!] Error: {e}")

driver.quit()

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False, encoding="utf-8-sig", sep=";", quoting=csv.QUOTE_ALL)