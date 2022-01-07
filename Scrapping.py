import pandas as pd
from bs4 import BeautifulSoup
from selenium import webDriver

driver = webdriver.Chrome(executable_path="/Users/aida/Desktop/Yearup/Mod3/CIS403/week18")
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()
for a in soup.findAll(attrs="blog-card__content-wrapper"):
    name =a.find("p")
    if date not in results:
        results.append(name.text)
for b in soup.findAll(attrs="blog-card__content-wrapper"):
    name =b.find("p")
    if date not in results:
        other_results.append(name.text)


df = pd.DataFrame({"Name":results})
df.to_csv('name.csv', index=False, encoding="utf-8")