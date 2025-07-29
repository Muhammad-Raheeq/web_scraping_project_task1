import os
import csv
from bs4 import BeautifulSoup

path = "basic"
news_data = []
for filename in os.listdir(path):
    if filename.endswith(".html"):
        file_path = os.path.join(path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            request=soup.find(class_="layout__item search__result-column u-2-of-3-lap-and-up u-1-of-1-portable")
            for h3 in request.find_all(['article']):
                headline = ""
                link = ""
                date = ""
                description=""
                a_tag = h3.find('h2')
                if a_tag and a_tag.get_text(strip=True):
                    headline = a_tag.get_text(strip=True)

                
                b_tag = h3.find('a')
                if b_tag and b_tag.has_attr('href'):
                    link = b_tag["href"]
                    if not link.startswith("http"):
                        link = "https://www.africanews.com" + link


                time_tag = h3.find('time')
                if time_tag:
                    date = time_tag.get_text(strip=True)

                description_tag=h3.find('p')
                if description_tag:
                    description=description_tag.get_text(strip=True)


                if headline:
                    news_data.append([headline, date, link,description])

output_csv = "African_news.csv"
with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Headline", "Date", "Link","description"])  
    writer.writerows(news_data)

print(f"Extracted {len(news_data)} news items and saved to '{output_csv}'")
