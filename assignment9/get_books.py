from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import json

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(url)
    sleep(3)  

    results = []

    # all elements
    books = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")
    print(f"Found {len(books)} book items")

    for book in books:
        try:
            title_elem = book.find_element(By.CLASS_NAME, "title-content")
            title = title_elem.text.strip()
        except:
            title = "N/A"

        try:
            author_elem = book.find_elements(By.CLASS_NAME, "author-link")
            authors = "; ".join([a.text.strip() for a in author_elem])
        except:
            authors = "N/A"

        try:
            format_elem = book.find_element(By.CLASS_NAME, "cp-format-info")
            format_year = format_elem.text.strip()
        except:
            format_year = "N/A"

        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    df = pd.DataFrame(results)
    print(df)

    # CSV
    df.to_csv("assignment9/get_books.csv", index=False)

    # JSON
    with open("assignment9/get_books.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

except Exception as e:
    print(f"Exception: {type(e).__name__} — {e}")
finally:
    driver.quit()
