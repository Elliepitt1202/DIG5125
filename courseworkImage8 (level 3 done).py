from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk
from tkinter import ttk

def update_image():
    # Get the current values from all sliders
    sharpness = float(sharpness_scale.get())
    bluriness = float(bluriness_scale.get())
    grayscale_factor = float(grayscale_scale.get())

    sharpness_int = int(sharpness)
    bluriness_int = int(bluriness)

    # Update the labels
    sharpness_value_label.config(text=f"Sharpness: {sharpness_int}")
    bluriness_value_label.config(text=f"Bluriness: {bluriness_int}")
    grayscale_value_label.config(text=f"Grayscale: {grayscale_factor:.2f}")

    # Apply Unsharp Mask filter for sharpness
    sharpened_image = original_image.filter(ImageFilter.UnsharpMask(radius=2, percent=sharpness_int * 2))

    # Apply Gaussian Blur filter for bluriness
    blurred_image = sharpened_image.filter(ImageFilter.GaussianBlur(bluriness_int))

    # Enhance grayscale with adjustable intensity
    grayscale_enhancer = ImageEnhance.Color(blurred_image)
    grayscale_image = grayscale_enhancer.enhance(grayscale_factor)

    photo = ImageTk.PhotoImage(grayscale_image)
    label.config(image=photo)
    label.image = photo

def reset_image():
    # Reset the image to its original state
    photo = ImageTk.PhotoImage(original_image)
    label.config(image=photo)
    label.image = photo
    sharpness_scale.set(0)
    bluriness_scale.set(0)
    grayscale_scale.set(0)

def close_application(event):
    root.destroy()

# Load the original image
image_path = "Images/rainbow1.jpg"
original_image = Image.open(image_path)

# Create the main window
root = tk.Tk()
root.title("Image Filters Sliders")

# Create a Tkinter PhotoImage from the original image
photo = ImageTk.PhotoImage(original_image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack(padx=10, pady=10)

# Create a slider for sharpness
sharpness_label = tk.Label(root, text="Sharpness:")
sharpness_label.pack()

sharpness_scale = ttk.Scale(root, from_=-100.0, to=100.0, orient=tk.HORIZONTAL, command=lambda x: update_image(), length=300)
sharpness_scale.set(0)  # Default sharpness value
sharpness_scale.pack(padx=10, pady=10)

sharpness_value_label = tk.Label(root, text="Sharpness: 0")
sharpness_value_label.pack()

# Create a slider for bluriness
bluriness_label = tk.Label(root, text="Bluriness:")
bluriness_label.pack()

bluriness_scale = ttk.Scale(root, from_=0.0, to=20.0, orient=tk.HORIZONTAL, command=lambda x: update_image(), length=300)
bluriness_scale.set(0)  # Default bluriness value
bluriness_scale.pack(padx=10, pady=10)

bluriness_value_label = tk.Label(root, text="Bluriness: 0")
bluriness_value_label.pack()

# Create a slider for grayscale effect
grayscale_label = tk.Label(root, text="Grayscale:")
grayscale_label.pack()

grayscale_scale = tk.Scale(root, from_=0.0, to=1.0, orient=tk.HORIZONTAL, command=lambda x: update_image(), length=300, resolution=0.01)
grayscale_scale.set(0)  # Default grayscale value
grayscale_scale.pack(padx=10, pady=10)

grayscale_value_label = tk.Label(root, text="Grayscale: 0.0")
grayscale_value_label.pack()

# Create a button to reset the image
reset_button = tk.Button(root, text="Reset Image", command=reset_image)
reset_button.pack(pady=10)

# Bind the 'q' key event to close the application
root.bind('<q>', close_application)

# Run the Tkinter event loop
root.mainloop()
