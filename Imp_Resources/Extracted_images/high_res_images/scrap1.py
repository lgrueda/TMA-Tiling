import requests
from bs4 import BeautifulSoup
import os

# Function to download an image given its URL
def download_image(image_url, save_folder, file_name):
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(os.path.join(save_folder, file_name), 'wb') as f:
            f.write(img_response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}")

# Function to scrape all the image links and download them
def scrape_images(base_url, save_folder):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the links for image details
    anchors = soup.find_all('a', href=True)  # Find all anchor tags with href
    for anchor in anchors:
        if "zoomify" in anchor['href']:  # Only select links leading to the zoomify viewer
            detail_page_url = "https://www.tissuearray.com" + anchor['href']
            print(f"Processing: {detail_page_url}")
            
            # Visit each detail page to get the high-resolution image
            detail_response = requests.get(detail_page_url)
            detail_soup = BeautifulSoup(detail_response.content, 'html.parser')
            
            # Find the image tag or link within the zoomify viewer
            img_tag = detail_soup.find('img')  # Adjust if necessary based on HTML structure
            if img_tag:
                high_res_image_url = img_tag['src']  # The actual image link
                image_name = anchor.text.strip() + ".jpg"  # Name the image based on its reference
                download_image(high_res_image_url, save_folder, image_name)
            else:
                print(f"No image found on {detail_page_url}")

# The base URL of the tissue microarray images
base_url = "https://www.tissuearray.com/tissue-arrays/Breast/BB08015"  # Example URL of TMA page

# Folder to save the downloaded images
save_folder = "./tissue_images"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Start the scraping and downloading process
scrape_images(base_url, save_folder)
