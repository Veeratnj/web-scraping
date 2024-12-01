import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Step 2: Visit the page
url = 'https://coinmarketcap.com/trending-cryptocurrencies/'  # Replace with the actual URL
driver.get(url)

# Step 3: Wait for the page to load
time.sleep(5)  # It's better to use WebDriverWait, but sleep is simpler for this example

# Step 4: Use XPath to locate the table element
xpath = '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/table'
table_element = driver.find_element(By.XPATH, xpath)

# Step 5: Extract all the rows from the table
rows = table_element.find_elements(By.TAG_NAME, 'tr')  # Find all rows

data1={"sino":[],
      "coin name":[],
      "price":[],
      "24h":[],
      "7d":[],
      "30d":[],
      "market cap":[],
      "volume":[],
      "last 7 days":[]}

# Step 6: Extract data from each row and cell
table_data = []
for row in rows:
    # print(row)
    cells = row.find_elements(By.TAG_NAME, 'td')  # Find all cells in each row
    
    row_data = [cell.text.strip() for cell in cells]  # Extract text from each cell
    if row_data:  # Only append non-empty rows
        data={"sino":0,
      "coin name":0,
      "price":0,
      "24h":0,
      "7d":0,
      "30d":0,
      "market cap":0,
      "volume":0,
      "last 7 days":0}

        data['sino']=row_data[1]
        data['coin name']=row_data[2]
        data['price']=row_data[3]
        data['24h']=row_data[4]
        data['7d']=row_data[5]
        data['30d']=row_data[6]
        data['market cap']=row_data[7]
        data['volume']=row_data[8]
        data['last 7 days']=row_data[9]
        print(row_data)
        # 5/0
        table_data.append(data)




# Step 7: Store the scraped table data as a JSON file
with open('table_data.json', 'w') as json_file:
    json.dump(table_data, json_file, indent=4)

print("Table data saved as table_data.json")

# Step 8: Close the WebDriver
driver.quit()
