Assignment Name: Image as Numbers
Description: Load an image, print shape, pixel values, channels, and explain them

---

1. Introduction

In computer vision, images are not stored as pictures but as numerical data. Each image is made up of pixels arranged in a grid. Each pixel contains intensity values that represent color.

---

2. Objective

To understand how images are represented as numerical arrays and analyze their structure including shape, pixel values, and channels.

---

3. Image Representation

An image is represented as a 3D array:

(height, width, channels)

Example: (100, 100, 3)

* Height → number of rows
* Width → number of columns
* Channels → color information

---

4. Pixel Values

Each pixel has values ranging from 0 to 255:

* 0 → Black
* 255 → White
* Values in between → Shades

For RGB images:

* Each pixel has 3 values → (R, G, B)

Example:
[255, 0, 0] → Red
[0, 255, 0] → Green
[0, 0, 255] → Blue

---

5. Channels

* Grayscale Image → 1 channel
* Color Image → 3 channels (Red, Green, Blue)

Each channel stores intensity for that color.

---

6. Data Type

Images are stored as integers (usually uint8), meaning values range from 0 to 255.

---

7. Pixel Range

The minimum and maximum values in the image show brightness range:

* Min value → darkest pixel
* Max value → brightest pixel

---

8. Working

The program:

* Loads an image
* Converts it into a numerical array
* Prints shape, pixel values, and channels
* Displays RGB channel values separately

---

9. Conclusion

Images are numerical representations of pixel data. Understanding this concept is essential for image processing, computer vision, and machine learning applications.

---
