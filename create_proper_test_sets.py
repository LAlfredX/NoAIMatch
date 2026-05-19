
import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageColor

# Create directories
base_dir = "test_images"

# Test set definitions
test_sets = [
    ("cats_with_dog", "cat", "dog"),
    ("dogs_with_cat", "dog", "cat"),
    ("cars_with_tree", "car", "tree"),
    ("trees_with_car", "tree", "car")
]

def create_cat_image(width=400, height=300, variation=0):
    """Create a cat-like image (orange color)"""
    img = Image.new('RGB', (width, height), color=(255, 165, 0))  # Orange
    draw = ImageDraw.Draw(img)
    
    # Add some variation
    np.random.seed(variation)
    for i in range(20):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        r = np.random.randint(5, 20)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(255, 140, 0))
    
    return img

def create_dog_image(width=400, height=300, variation=0):
    """Create a dog-like image (brown color)"""
    img = Image.new('RGB', (width, height), color=(139, 69, 19))  # Brown
    draw = ImageDraw.Draw(img)
    
    # Add some variation
    np.random.seed(variation + 100)
    for i in range(20):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        r = np.random.randint(5, 20)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(160, 82, 45))
    
    return img

def create_car_image(width=400, height=300, variation=0):
    """Create a car-like image (blue color)"""
    img = Image.new('RGB', (width, height), color=(30, 144, 255))  # Blue
    draw = ImageDraw.Draw(img)
    
    # Add some variation
    np.random.seed(variation + 200)
    for i in range(20):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        r = np.random.randint(5, 20)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(65, 105, 225))
    
    return img

def create_tree_image(width=400, height=300, variation=0):
    """Create a tree-like image (green color)"""
    img = Image.new('RGB', (width, height), color=(34, 139, 34))  # Green
    draw = ImageDraw.Draw(img)
    
    # Add some variation
    np.random.seed(variation + 300)
    for i in range(20):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        r = np.random.randint(5, 20)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(60, 179, 113))
    
    return img

# Image creation functions
image_functions = {
    "cat": create_cat_image,
    "dog": create_dog_image,
    "car": create_car_image,
    "tree": create_tree_image
}

# Process each test set
for test_set_name, main_object, intruder_object in test_sets:
    test_dir = os.path.join(base_dir, test_set_name)
    
    # Clear if exists
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir, exist_ok=True)
    
    print(f"\nCreating test set: {test_set_name}")
    
    # Create 8 variations of the main object
    for i in range(8):
        img_func = image_functions[main_object]
        img = img_func(variation=i)
        filename = f"{main_object}_{i:02d}.png"
        img.save(os.path.join(test_dir, filename))
        print(f"  - {filename}")
    
    # Add 1 intruder (different object)
    intruder_img_func = image_functions[intruder_object]
    intruder_img = intruder_img_func(variation=99)
    intruder_filename = f"{intruder_object}_intruder.png"
    intruder_img.save(os.path.join(test_dir, intruder_filename))
    print(f"  - {intruder_filename} (INTRUDER)")

print("\nTest sets created with distinct object images!")
print("\nObject colors:")
print("  Cat: Orange")
print("  Dog: Brown")
print("  Car: Blue")
print("  Tree: Green")
