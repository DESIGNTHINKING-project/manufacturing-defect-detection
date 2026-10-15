
import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found. Please check the file name.")
else:
    # Convert BGR to RGB for correct colors
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the image
    plt.imshow(image)
    plt.title("Manufacturing Image")
    plt.axis("off")
    plt.show()
