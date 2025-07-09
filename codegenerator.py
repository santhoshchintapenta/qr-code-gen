import qrcode

# Step 1: Get user input
data = input("Enter the text or URL to generate QR code: ")

# Step 2: Create QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    box_size=10,
    border=5
)

# Step 3: Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Step 4: Create image
img = qr.make_image(fill_color="black", back_color="white")

# Step 5: Save the image
file_name = "my_qr_code.png"
img.save(file_name)

print(f"QR Code saved as '{file_name}'")
