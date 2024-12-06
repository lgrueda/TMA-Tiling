import os
import cv2

# Define the size you want to resize to (224x224 or 256x256)
target_size = (224, 224)  # Change this to (256, 256) if needed

# Set paths for input and output directories
input_folder = "in_images/"   # Folder with original images (screenshots)
output_folder = "re_images1/"  # Folder where resized images will be saved

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Add more formats if needed
        image_path = os.path.join(input_folder, filename)
        
        # Read the image
        image = cv2.imread(image_path)
        
        # Check if image is loaded properly
        if image is not None:
            # Resize the image
            resized_image = cv2.resize(image, target_size)
            
            # Save the resized image in the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_image)
            print(f"Resized and saved: {filename}")
        else:
            print(f"Failed to load image: {filename}")
