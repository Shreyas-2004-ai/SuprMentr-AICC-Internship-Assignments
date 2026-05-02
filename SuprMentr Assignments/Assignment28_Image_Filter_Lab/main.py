import cv2

# Load image
img = cv2.imread("sample.jpg")

# Check if image loaded
if img is None:
    print("Error: Image not found!")
    exit()

# -----------------------------
# GRAYSCALE
# -----------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# BLUR
# -----------------------------
blur = cv2.GaussianBlur(img, (5, 5), 0)

# -----------------------------
# EDGE DETECTION
# -----------------------------
edges = cv2.Canny(img, 100, 200)

# -----------------------------
# SHOW IMAGES
# -----------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Edge Detection", edges)

# Wait until key press
cv2.waitKey(0)
cv2.destroyAllWindows()