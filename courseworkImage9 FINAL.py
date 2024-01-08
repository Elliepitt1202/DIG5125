from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk
from tkinter import ttk

# Function to update the displayed image based on the slider values
def update_image():
    sharpness, bluriness, grayscale_factor = map(float, (sharpness_scale.get(), bluriness_scale.get(), grayscale_scale.get()))
    sharpness_int, bluriness_int = int(sharpness), int(bluriness)

    # Update labels with current slider values
    sharpness_value_label.config(text=f"Sharpness: {sharpness_int}")
    bluriness_value_label.config(text=f"Bluriness: {bluriness_int}")
    grayscale_value_label.config(text=f"Grayscale: {grayscale_factor:.2f}")

    # Apply filters to the original image
    sharpened_image = original_image.filter(ImageFilter.UnsharpMask(radius=2, percent=sharpness_int * 2))
    blurred_image = sharpened_image.filter(ImageFilter.GaussianBlur(bluriness_int))
    grayscale_image = ImageEnhance.Color(blurred_image).enhance(grayscale_factor)

    # Update the displayed image
    update_display(grayscale_image)

# Function to apply edge detection filter
def apply_edge_detection():
    edges_image = original_image.filter(ImageFilter.FIND_EDGES)
    edges_image = ImageEnhance.Contrast(edges_image).enhance(2.0)
    update_display(edges_image)

# Function to apply edge enhancement filter
def apply_edge_enhance():
    edge_enhance_image = original_image.filter(ImageFilter.EDGE_ENHANCE)
    update_display(edge_enhance_image)

# Function to apply Gaussian blur with a fixed radius
def apply_gaussian_blur_button():
    blur_radius = 5
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    update_display(blurred_image)

# Function to apply a smoothing filter
def apply_smoothing_filter():
    smoothed_image = original_image.filter(ImageFilter.SMOOTH)
    update_display(smoothed_image)

# Function to apply an embossing filter
def apply_emboss_filter():
    embossed_image = original_image.filter(ImageFilter.EMBOSS)
    update_display(embossed_image)

# Function to reset the image to its original state
def reset_image():
    update_display(original_image)
    sharpness_scale.set(0)
    bluriness_scale.set(0)
    grayscale_scale.set(1.0)

# Function to close the application when pressing "q"
def close_application(event):
    root.destroy()

# Function to update the displayed image
def update_display(image):
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

# Load the original image
image_path = "Images/rainbow1.jpg"
original_image = Image.open(image_path)

# Create the main window
root = tk.Tk()
root.title("Image Filters Sliders")
root.configure(bg='pink')

# Create a Tkinter Photo Image from the original image
photo = ImageTk.PhotoImage(original_image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack(padx=10, pady=10)

# Function to create a slider frame with label and value label
def slider_frame(parent, label_text, scale_from, scale_to, scale_command, default_value):
    frame = ttk.Frame(parent)
    frame.pack(pady=10)

    label = tk.Label(frame, text=label_text)
    label.pack()

    scale = ttk.Scale(frame, from_=scale_from, to=scale_to, orient=tk.HORIZONTAL, command=scale_command, length=300)
    scale.set(default_value)
    scale.pack(padx=10, pady=10)

    value_label = tk.Label(frame, text=f"{label_text}: {default_value}")
    value_label.pack()

    return scale, value_label

# Create slider frames for Sharpness, Bluriness, and Grayscale
sharpness_scale, sharpness_value_label = slider_frame(root, "Sharpness", -100.0, 100.0, lambda x: update_image(), 0)
bluriness_scale, bluriness_value_label = slider_frame(root, "Bluriness", 0.0, 20.0, lambda x: update_image(), 0)
grayscale_scale, grayscale_value_label = slider_frame(root, "Grayscale", 0.0, 1.0, lambda x: update_image(), 1.0)

# Create buttons for each filter
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = [
    ("Edge Detection", apply_edge_detection),
    ("Edge Enhance", apply_edge_enhance),
    ("Gaussian Blur", apply_gaussian_blur_button),
    ("Smoothing Filter", apply_smoothing_filter),
    ("Emboss Filter", apply_emboss_filter),
]

# Create buttons using a loop
for button_text, button_command in buttons:
    button = tk.Button(button_frame, text=button_text, command=button_command)
    button.pack(side=tk.LEFT, padx=5)

# Create a reset button
reset_button = tk.Button(root, text="Reset Image", command=reset_image)
reset_button.pack(pady=10)

# Key "q" to close the application
root.bind('<q>', close_application)

# Run the Tkinter event loop
root.mainloop()
