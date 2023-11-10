import pyzbar.pyzbar as pyzbar
import cv2

# Read the image file
image =image = cv2.imread("C:/Users/anike/OneDrive/Desktop/Qr_code/scan_me.jpg")

# Decode the QR code
decoded = pyzbar.decode(image)

# Print the data contained in the QR code
print(decoded[0].data.decode("utf-8"))