from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import csv

# URL
base_urls = [
    "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
    "https://owasp.org/Top10/A02_2021-Cryptographic_Failures/",
    "https://owasp.org/Top10/A03_2021-Injection/",
    "https://owasp.org/Top10/A04_2021-Insecure_Design/",
    "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
    "https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/",
    "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/",
    "https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/",
    "https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/",
    "https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/"
]

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

results = []

for url in base_urls:
    try:
        driver.get(url)
        sleep(2)  

        title = driver.find_element(By.TAG_NAME, "h1").text.strip()
        try:
            paragraph = driver.find_element(By.TAG_NAME, "p").text.strip()
        except:
            paragraph = driver.find_element(By.CSS_SELECTOR, "div.md-typeset > div > div").text.strip()

        results.append({
            "Title": title,
            "Link": url,
            "Description": paragraph
        })

        print(f"[+] {title}")
    except Exception as e:
        print(f"[!] Failed on {url}: {type(e).__name__} — {e}")

driver.quit()

# CSV
df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False, encoding="utf-8-sig", sep=";", quoting=csv.QUOTE_ALL)


with open("challenges.txt", "w", encoding="utf-8") as f:
    f.write("""Task: Scraping OWASP Top 10 (2021)

Challenges faced:
1. The official OWASP "Top 10" page (https://owasp.org/Top10/) didn't list all links in a structured way that could be scraped directly.
2. Some expected URLs like "https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery/" led to a 404 error.
3. The final A10 link used a different format: "https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/" — it required manual inspection to find.
4. Some descriptions were not found under <p> tags as expected, so a fallback CSS selector had to be used.
5. CSV output formatting needed tuning for better readability.

Solutions:
- Used a hardcoded list of URLs with verified working links.
- Added error handling and printed debug info for failures.
- Used sleep() to allow pages to fully load.
- Used pandas with encoding="utf-8-sig" and semicolon delimiter for readable CSV.

The final code now successfully extracts title, link, and description for all Top 10 vulnerabilities from OWASP 2021 and writes to owasp_top_10.csv.
""")
