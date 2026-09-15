import requests
import csv
import time
from bs4 import BeautifulSoup

class Scraper:
    def __init__ (self,url):
        self.url = url

    def fetch(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Network Error:{e}")
            return None
class Parser:
    def __init__(self,html):
        self.html = html
    def parse(self):
        soup = BeautifulSoup(self.html,'html.parser')   
        items = soup.find_all('div',class_='quote')
        data = []
        for item in items:
            text = item.find('span',class_='text').get_text()
            author = item.find('small',class_='author').get_text()
            data.append({'text': text,'author': author})
            return data
       
           
class DataSaver:
    def __init__(self,filepath):
        self.filepath = filepath
    def save(self,data):
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['text', 'author'])
            writer.writeheader()
            writer.writerows(data)

if __name__ == "__main__":
    url = input("Enter URL: ")
    scraper = Scraper(url)
    html = scraper.fetch()
    if html:
        parser = Parser(html)
        data = parser.parse()
        if data:
            saver = DataSaver('scraped_data.csv')
            saver.save(data)
            print('Saved')
    


        
                             

