import requests
import selectorlib
from send_email import Email
import time
import dbHelper

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scrape(this, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(this, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Store:
    def get_sended_emails(this):
        with open("data.txt", "r") as file:
            return file.read()

    def store(this, data):
        with open("data.txt", "a") as file:
            file.write(extracted + "\n")



if __name__ == "__main__":
    event = Event()
    store = Store()
    email = Email()
    dbh = dbHelper.DbHelper(database_path="data.db")
    while True:
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        row = extracted.split(",")
        row = [item.strip() for item in row]
        if extracted.lower() != "no upcoming tours":
            historical = store.get_sended_emails()
            if not dbh.event_in_table(row):
                email.send(extracted)
                #store(extracted)
                dbh.insert_sigle("events", row)
        print(extracted)
        time.sleep(5)


