from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
import pandas as pd

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
file = 0

for i in range(1, 11):
    driver.get(f"https://merojob.com/category/teaching-education/?page={i}")
    time.sleep(0)
    
    elems1 = driver.find_elements(By.CLASS_NAME, "card-footer")
    elems2=driver.find_elements(By.CLASS_NAME, "row")
    if elems2: 
        div class_="row":
    print(f"{len(elems1)} items found:1")
    print(f"{len(elems2)} items found:2")
    for elem in elems1:
        d = elem.get_attribute("outerHTML")
        with open(f"data/page_{i}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

time.sleep(3)
driver.close()
