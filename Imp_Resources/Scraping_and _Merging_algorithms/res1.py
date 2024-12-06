import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the ESRGAN model from TensorFlow Hub
model = hub.load('https://tfhub.dev/captain-pool/esrgan-tf2/1')

# Load your low-resolution image (path to the image you uploaded)
low_res_image_path = 'img\download.png'  # Your uploaded image path
low_res_image = cv2.imread(low_res_image_path)

# Convert the image to RGB
low_res_image = cv2.cvtColor(low_res_image, cv2.COLOR_BGR2RGB)

# Normalize and prepare image for the model
low_res_image = np.array(low_res_image).astype(np.float32) / 255.0
low_res_image = np.expand_dims(low_res_image, axis=0)  # Add batch dimension

# Generate a high-resolution image using ESRGAN
high_res_image = model(low_res_image)
high_res_image = tf.squeeze(high_res_image)  # Remove batch dimension
high_res_image = tf.clip_by_value(high_res_image, 0.0, 1.0).numpy()

# Convert the high-res image back to an 8-bit format
high_res_image = (high_res_image * 255).astype(np.uint8)

# Display the high-res image
plt.imshow(high_res_image)
plt.axis('off')
plt.show()

# Save the high-resolution image
high_res_image = cv2.cvtColor(high_res_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('/res_image/high_res_image.png', high_res_image)
