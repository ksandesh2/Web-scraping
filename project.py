from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = "laptop"
file = 0

for i in range(1, 3):
    driver.get(f"https://www.daraz.com.np/catalog/?page={i}&q={query}&spm=a2a0e.tm80335409.search.d_go")

    elems = driver.find_elements(By.CLASS_NAME, "buTCk")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

    time.sleep(2)
driver.close()
