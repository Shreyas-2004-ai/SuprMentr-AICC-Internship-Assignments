import time
import numpy as np

# Create 1 million numbers
size = 1_000_000

# Python list
python_list = list(range(size))

# NumPy array
numpy_array = np.arange(size)

# --- Python List Test ---
start = time.time()
python_result = [x * 2 for x in python_list]
end = time.time()
python_time = end - start

# --- NumPy Array Test ---
start = time.time()
numpy_result = numpy_array * 2
end = time.time()
numpy_time = end - start

# Results
print("\n--- Speed Test Results ---")
print(f"Python List Time: {python_time:.6f} seconds")
print(f"NumPy Array Time: {numpy_time:.6f} seconds")