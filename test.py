import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
url = 'https://www.nba.com/stats/players/passing?Season=2015-16'

# navigate to the page
driver.get(url)

# toggle 'all'
time.sleep(2)
dropdown = Select(driver.find_elements(By.TAG_NAME, 'select')[-1])
dropdown.select_by_index(0)

# print("Parsing: " + name + " " + season)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# extract data table
table = soup.find_all('table')
table = table[-1]

columns = []
data = []

# Extract column names from the table header
for header in table.find_all('th'):
    columns.append(header.text.strip().replace('\xa0', ''))

# Extract data from the table rows
for row in table.find_all('tr')[1:]:  # Skip the header row
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    data.append(row_data)
print(data)