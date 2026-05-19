
import os
import shutil
import numpy as np
from PIL import Image

# Create test sets
test_sets = [
    ("cats_with_dog", "british_shorthair", "labrador"),
    ("dogs_with_cat", "labrador", "british_shorthair"),
    ("cars_with_tree", "car", "tree"),
    ("trees_with_car", "tree", "car")
]

# Source directories
source_dir = "test_images/small_test"
base_image = os.path.join(source_dir, "original.png")

# Load base image
img = Image.open(base_image)

# Function to create variations (same object, slightly different)
def create_variation(img, i, seed=42):
    img_arr = np.array(img)
    
    # Add slight noise and brightness variation
    np.random.seed(seed + i)
    noise = np.random.normal(0, 5, img_arr.shape).astype(np.int16)
    img_arr = np.clip(img_arr + noise, 0, 255).astype(np.uint8)
    
    # Adjust brightness
    brightness = 0.9 + (i % 5) * 0.05
    img_arr = np.clip(img_arr * brightness, 0, 255).astype(np.uint8)
    
    return Image.fromarray(img_arr)

# Function to create different object (inverted colors)
def create_different_object(img):
    img_arr = np.array(img)
    # Invert colors to look like a completely different object
    return Image.fromarray(255 - img_arr)

# Process each test set
for test_set_name, main_object, intruder_object in test_sets:
    test_dir = os.path.join("test_images", test_set_name)
    
    # Clear if exists
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir, exist_ok=True)
    
    print(f"Creating test set: {test_set_name}")
    
    # Create 8 variations of the main object
    for i in range(8):
        var_img = create_variation(img, i, seed=42)
        filename = f"{main_object}_{i:02d}.png"
        var_img.save(os.path.join(test_dir, filename))
        print(f"  - {filename}")
    
    # Add 1 intruder (different object)
    intruder_img = create_different_object(img)
    intruder_filename = f"{intruder_object}_intruder.png"
    intruder_img.save(os.path.join(test_dir, intruder_filename))
    print(f"  - {intruder_filename} (INTRUDER)")

print("\nTest sets created successfully!")
