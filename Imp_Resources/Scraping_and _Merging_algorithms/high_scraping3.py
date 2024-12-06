import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the page containing the list of tissue samples (table)
page_url = 'https://www.tissuearray.com/tissue-arrays/Breast/BB08015'

# Directory to save the high-resolution images
output_dir = 'high_res_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to download an image from a given URL
def download_image(img_url, output_dir, img_name):
    try:
        # Get image data
        response = requests.get(img_url)
        # Check if the response is an image
        if 'image' in response.headers['Content-Type']:
            # Add the correct image extension if missing
            content_type = response.headers['Content-Type'].split('/')[-1]
            img_name = f"{img_name}.{content_type}"
            img_path = os.path.join(output_dir, img_name)
            
            # Save the image
            with open(img_path, 'wb') as handler:
                handler.write(response.content)
            
            print(f"Downloaded: {img_name}")
        else:
            print(f"Failed to download {img_name}: URL does not point to an image")
    except Exception as e:
        print(f"Failed to download {img_name}: {e}")

# Get the HTML content of the main page
response = requests.get(page_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Base URL for the website
base_url = "https://www.tissuearray.com/"

# Find all the clickable links (e.g., A1, A2, B1, etc.) that lead to detailed image pages
links = soup.select('table tbody tr td a')  # Adjust this selector based on the table structure

if not links:
    print("No links found. The structure might have changed.")
    exit()

# Loop through each link to visit its respective page and download the high-resolution image
for link in links:
    sample_name = link.text.strip()  # Get the text of the link (e.g., A1, A2)
    detail_page_url = urljoin(base_url, link['href'])  # Construct the URL for the detailed image page

    # Debugging print to ensure correct URL for the sample
    print(f"Visiting page for {sample_name}: {detail_page_url}")
    
    # Get the HTML content of the detailed image page
    detail_response = requests.get(detail_page_url)
    if detail_response.status_code == 200:
        detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

        # Find the zoomify image link
        zoomify_link = detail_soup.find('a', text="Full Page")  # Look for the 'Full Page' link to get high-res
        if zoomify_link:
            img_url = urljoin(base_url, zoomify_link['href'])
            # Debugging print to verify high-res image URL
            print(f"High-res image URL for {sample_name}: {img_url}")
            
            # Download the high-resolution image from the zoomify URL
            download_image(img_url, output_dir, sample_name)
        else:
            print(f"No high-res zoomify link found for {sample_name}")
    else:
        print(f"Failed to load detailed page for {sample_name}. Status code: {detail_response.status_code}")

print("High-resolution image scraping completed!")
