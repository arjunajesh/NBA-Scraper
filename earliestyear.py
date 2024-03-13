from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

def earliest_season(link):
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(1)
    dropdown = Select(driver.find_elements(By.TAG_NAME, 'select')[0])
    earliest = int(dropdown.options[-1].text[:4])
    return earliest 


def earliest_common_season(links):
    print("Starting search...")
    earliest = 0
    for link in links:
        print("Searching: " + link)
        season = earliest_season(link)
        print("Earliest season: " + str(season))
        earliest = max(earliest, season)
    return earliest

