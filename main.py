import requests
import selectorlib
from send_email import send_email
import time

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value



def store(data):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def get_sended_emails():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        if extracted.lower() != "no upcoming tours":
            historical = get_sended_emails()
            if extracted not in historical:
                send_email(extracted)
                store(extracted)
        print(extracted)
        time.sleep(5)


