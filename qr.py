import tkinter as tk
import qrcode
from PIL import ImageTk, Image

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    img = ImageTk.PhotoImage(qr_image)
    qr_code_image.config(image=img)
    qr_code_image.image = img

# Create main app
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("360x480")  # Adjust the window size as needed

# Set a background color
app.configure(bg="#E0E0E0")

# Create a label with Android-like style
label = tk.Label(
    app,
    text="Enter the data:",
    font=("Roboto", 16),
    bg="#E0E0E0",  # Use a light gray color
)
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(
    app,
    font=("Roboto", 14),
    bg="white",
)
entry.pack(fill=tk.BOTH, padx=20)

# Create a button with Android-like style
generate_button = tk.Button(
    app,
    text="Generate QR Code",
    font=("Roboto", 14),
    bg="#6200EE",  # Use a deep purple color
    fg="white",
    command=generate_qr_code,
)
generate_button.pack(pady=10)

# Create an image label
qr_code_image = tk.Label(app, bg="#E0E0E0")
qr_code_image.pack()

# Run the app
app.mainloop()
