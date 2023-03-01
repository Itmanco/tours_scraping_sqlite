import requests
import selectorlib
import time
import dbHelper

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperatureId"]
    return value


def store(data):
    with open("temperaturedata.txt", "a") as file:
        file.write(data + "\n")



if __name__ == "__main__":
    if (dbHelper.query_all("temperatures_times") == "no such table"):
        dbHelper.create_table("temperatures_times", [("Date", "str"), ("temperature", "int")])

    while True:
        now = time.time()
        #now = time.strftime("%y-%m-%d-%H-%M-%S")+","
        now = time.strftime("%y-%m-%d-%H-%M-%S")

        scraped = scrape(URL)
        extracted = extract(scraped)

        #store(now+extracted)
        dbHelper.insert_sigle("temperatures_times",[now,int(extracted)])
        print(now+","+extracted)
        time.sleep(2)
