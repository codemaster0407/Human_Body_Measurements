import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_background(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper threshold values for the background color
    lower_threshold = np.array([0, 0, 0])  # Adjust these values according to the background color
    upper_threshold = np.array([180, 255, 100])  # Adjust these values according to the background color

    # Create a mask based on the defined threshold values
    mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)

    # Apply bitwise-and operation to extract the foreground
    foreground = cv2.bitwise_and(image, image, mask=mask)

    # Create a white background image
    background = np.ones_like(image) * 255

    # Subtract the foreground from the background to obtain the image with the background removed
    removed_background = cv2.subtract(background, foreground)

    return removed_background



image_path = 'Photos\\all_photos\\IMG-20230614-WA0006.jpg'
bg_remove = remove_background(image_path)
plt.imshow(bg_remove)
plt.show()