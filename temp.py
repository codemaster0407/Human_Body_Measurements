import cv2
import matplotlib.pyplot as plt
import numpy as np

dense_pose = cv2.imread("D:\\Virtual Tryon\\outputres.0001.png")
# plt.imshow(dense_pose)
# plt.show()

# Convert BGR to RGB
image_rgb = cv2.cvtColor(dense_pose, cv2.COLOR_BGR2RGB)

grayscale_image = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
plt.imshow(grayscale_image, cmap = 'gray')

plt.show()