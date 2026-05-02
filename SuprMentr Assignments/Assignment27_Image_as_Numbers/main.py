from PIL import Image
import numpy as np

# Load image
img = Image.open("sample.jpg")

# Convert to numpy array
img_array = np.array(img)

# -----------------------------
# BASIC INFO
# -----------------------------
print("📌 Image Shape (Height, Width, Channels):", img_array.shape)
print("📌 Data Type:", img_array.dtype)

# -----------------------------
# PIXEL VALUES
# -----------------------------
print("\n📌 Sample Pixel Values (Top-left 3x3 area):")
print(img_array[:3, :3])

# -----------------------------
# CHANNEL INFO
# -----------------------------
if len(img_array.shape) == 3:
    print("\n📌 Number of Channels:", img_array.shape[2])
    print("👉 RGB Channels Explanation:")
    print("Red channel sample:\n", img_array[:3, :3, 0])
    print("Green channel sample:\n", img_array[:3, :3, 1])
    print("Blue channel sample:\n", img_array[:3, :3, 2])
else:
    print("\n📌 Grayscale Image (Single Channel)")

# -----------------------------
# PIXEL RANGE
# -----------------------------
print("\n📌 Pixel Value Range:")
print("Min:", img_array.min())
print("Max:", img_array.max())

# -----------------------------
# IMAGE SIZE
# -----------------------------
height, width = img_array.shape[:2]
print("\n📌 Image Size:")
print("Height:", height)
print("Width:", width)

# -----------------------------
# TOTAL PIXELS
# -----------------------------
print("\n📌 Total Pixels:", height * width)