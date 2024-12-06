from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import time

# Path to your ChromeDriver (update this path accordingly)
driver_path = r'C:\Users\kavya\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe'

# Create a Service instance and initialize the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL of the page to scrape
url = 'https://www.tissuearray.com/tissue-arrays/Breast/BR1006a'

# Navigate to the page
driver.get(url)

# Wait for the page to fully load (adjust time or use WebDriverWait as needed)
time.sleep(5)

# Locate and print the number of rows to check if they are identified
rows = driver.find_elements(By.TAG_NAME, 'tr')
print(f"Total rows found: {len(rows)}")

# Prepare to write data to a CSV file
with open('2nd_set.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header row if it exists
    header_row = rows[0].find_elements(By.TAG_NAME, 'th')
    header = [th.text.strip() for th in header_row]
    writer.writerow(header)
    
    # Iterate over each row in the table
    for row in rows[1:]:  # Skip the header row
        cells = row.find_elements(By.TAG_NAME, 'td')
        
        # Extract and print cell contents
        cell_data = [cell.text.strip() for cell in cells]
        print("Cells content:", cell_data)
        
        # Write the data to the CSV file
        writer.writerow(cell_data)

# Close the WebDriver
driver.quit()

print("CSV file '2nd_set.csv' created successfully.")
