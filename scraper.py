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

def get_data(name, link, seasons):
    driver = webdriver.Chrome()
    pages = {}
    for season in seasons:
        while True:
            try:
                print("Scraping: " + name + " " + season)
                url = link + season
                # navigate to the page
                driver.get(url)

                # toggle 'all'
                time.sleep(2)
                dropdown = Select(driver.find_elements(By.TAG_NAME, 'select')[-1])
                dropdown.select_by_index(0)

                print("Parsing: " + name + " " + season)
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                # extract data table
                table = soup.find_all('table')
                table = table[-1]

                columns = []
                data = []

                # Extract column names from the table header
                for header in table.find_all('th'):
                    txt = header.text.strip().replace('\xa0', '')
                    if txt not in columns:
                        columns.append(header.text.strip().replace('\xa0', ''))

                if columns[0] == "Sun":
                    raise Exception()
                
                if name == "box_scores":
                    columns = columns[:30]

                # Extract data from the table rows
                for row in table.find_all('tr')[1:]:  # Skip the header row
                    row_data = [cell.text.strip() for cell in row.find_all('td')]
                    data.append(row_data)
                # print(data)

                # Create a Pandas DataFrame
                df = pd.DataFrame(data, columns=columns)

                print("Writing: " + name + " " + season)
                path = os.path.join(os.getcwd(), season, name + '.csv')
                df.to_csv(path, index=False)
            except:
                print("Error, trying again")
                driver.quit()
                driver.get(url)
                continue
            else:
                break
    # Close the browser
    driver.quit()
    print("Finished scraping: " + name)

    # for season, page_source in pages.items():
    print("Finished: " + name)

# driver = webdriver.Chrome()
# url = 'https://www.nba.com/stats/players/traditional?Season=2015-16'

# # navigate to the page
# driver.get(url)

# # toggle 'all'
# print("done")
# time.sleep(1)
# dropdown = Select(driver.find_elements(By.TAG_NAME, 'select')[-1])
# dropdown.select_by_index(0)


# # save the page source
# page = driver.page_source
# # print(page)
# # Close the browser
# driver.quit()

# soup = BeautifulSoup(page, 'html.parser')

# # extract data table
# table = soup.find_all('table')[-1]
# # print(len(table))

# columns = []
# data = []

# # Extract column names from the table header
# for header in table.find_all('th'):
#     columns.append(header.text.strip().replace('\xa0', ''))

# # if name == "box_scores":
# columns = columns[:30]

# # Extract data from the table rows
# for row in table.find_all('tr')[1:]:  # Skip the header row
#     row_data = [cell.text.strip() for cell in row.find_all('td')]
#     data.append(row_data)


# df = pd.DataFrame(data, columns=columns)

# # print("Writing: " + name + " " + season)
# path = os.path.join(os.getcwd(), "2015-16", "box_scores" + '.csv')
# df.to_csv(path, index=False)