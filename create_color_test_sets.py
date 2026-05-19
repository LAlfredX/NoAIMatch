
import os
import shutil
import numpy as np
from PIL import Image, ImageDraw

# Create directories
base_dir = "test_images"

# Test set definitions - use color-based names
test_sets = [
    ("yellow_with_blue", "yellow_bubble", "blue_bubble"),
    ("blue_with_yellow", "blue_bubble", "yellow_bubble"),
    ("green_with_red", "green_bubble", "red_bubble"),
    ("red_with_green", "red_bubble", "green_bubble")
]

def create_yellow_bubble(width=400, height=300, variation=0):
    """Create a yellow bubble image"""
    img = Image.new('RGB', (width, height), color=(255, 215, 0))  # Golden yellow
    draw = ImageDraw.Draw(img)
    
    # Add some bubble variation
    np.random.seed(variation)
    for i in range(15):
        x = np.random.randint(50, width-50)
        y = np.random.randint(50, height-50)
        r = np.random.randint(20, 50)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(255, 255, 0))
    
    return img

def create_blue_bubble(width=400, height=300, variation=0):
    """Create a blue bubble image"""
    img = Image.new('RGB', (width, height), color=(30, 144, 255))  # Blue
    draw = ImageDraw.Draw(img)
    
    # Add some bubble variation
    np.random.seed(variation + 100)
    for i in range(15):
        x = np.random.randint(50, width-50)
        y = np.random.randint(50, height-50)
        r = np.random.randint(20, 50)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(65, 105, 225))
    
    return img

def create_green_bubble(width=400, height=300, variation=0):
    """Create a green bubble image"""
    img = Image.new('RGB', (width, height), color=(34, 139, 34))  # Green
    draw = ImageDraw.Draw(img)
    
    # Add some bubble variation
    np.random.seed(variation + 200)
    for i in range(15):
        x = np.random.randint(50, width-50)
        y = np.random.randint(50, height-50)
        r = np.random.randint(20, 50)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(60, 179, 113))
    
    return img

def create_red_bubble(width=400, height=300, variation=0):
    """Create a red bubble image"""
    img = Image.new('RGB', (width, height), color=(220, 20, 60))  # Red
    draw = ImageDraw.Draw(img)
    
    # Add some bubble variation
    np.random.seed(variation + 300)
    for i in range(15):
        x = np.random.randint(50, width-50)
        y = np.random.randint(50, height-50)
        r = np.random.randint(20, 50)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(255, 69, 0))
    
    return img

# Image creation functions
image_functions = {
    "yellow_bubble": create_yellow_bubble,
    "blue_bubble": create_blue_bubble,
    "green_bubble": create_green_bubble,
    "red_bubble": create_red_bubble
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

print("\nTest sets created with color bubble images!")
print("\nBubble colors:")
print("  Yellow Bubble: Gold/Yellow")
print("  Blue Bubble: Blue")
print("  Green Bubble: Green")
print("  Red Bubble: Red")
