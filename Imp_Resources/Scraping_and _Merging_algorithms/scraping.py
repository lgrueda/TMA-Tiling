import os
import requests
from bs4 import BeautifulSoup

# URL of the page containing the images
page_url = 'https://www.tissuearray.com/tissue-arrays/Breast/BB08015'

# Directory to save the scraped images
output_dir = 'scraped_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to download an image from a given URL
def download_image(img_url, output_dir):
    # Get image data
    img_data = requests.get(img_url).content
    
    # Extract image name from the URL
    img_name = img_url.split('/')[-1]
    
    # Create full output path
    img_path = os.path.join(output_dir, img_name)
    
    # Save the image
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    
    print(f"Downloaded: {img_name}")

# Get the HTML content of the page
response = requests.get(page_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Base URL for high-resolution images (if needed)
base_url = "https://www.tissuearray.com/"

# Find all image tags
images = soup.find_all('img')

# Download each image
for img in images:
    img_url = img['src']
    
    # Handle relative URLs
    if not img_url.startswith('http'):
        img_url = base_url + img_url
    
    # Check for higher-resolution images (e.g., sometimes 'zoomify' or 'large' in URL path)
    # Here, you can modify the URL pattern to download the high-resolution version
    if 'zoomify' in img_url:
        high_res_url = img_url.replace('zoomify', 'full')  # Example modification, adjust based on URL pattern
        download_image(high_res_url, output_dir)
    else:
        download_image(img_url, output_dir)

print("Image scraping completed!")
