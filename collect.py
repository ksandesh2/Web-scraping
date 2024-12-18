from bs4 import BeautifulSoup
import os
import pandas as pd
d={'title':[], 'Link':[] ,'Price':[], 'Items sold':[], 'Province':[], 'Rating':[] }
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t=soup.find("a")
        if t:
            title=t.get_text()
            link = t.get("href")
        p=soup.find("span", class_="ooOxS")
        price=p.get_text()
        i=soup.find("span", class_="_1cEkb")
        items=i.get_text()
        s=soup.find("span", class_="oa6ri")
        province=s.get_text()
        f=soup.find("span", class_="qzqFw")
        rating=f.get_text()
        print(title, link, price, items, province, rating)
        d['title'].append(title)
        d['Link'].append(link)
        d['Price'].append(price)
        d['Items sold'].append(items)
        d['Province'].append(province)
        d['Rating'].append(rating)
    except Exception as e:
        print(e)
df=pd.DataFrame(data=d)
df.to_csv("data.csv")