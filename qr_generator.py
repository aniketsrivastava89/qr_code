import qrcode
# import Image

# Read the data for the QR code from the user
data = input("Enter the data for the QR code: ")

# Create the QR code object
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Add the data to the QR code object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("scan_me.jpg")

print("QR code saved to scan_me.jpg")