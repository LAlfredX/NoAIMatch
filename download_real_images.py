
import os
import requests
from PIL import Image
from io import BytesIO
import numpy as np

# Download images from free public sources
def download_image(url, filename, save_dir):
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        img = img.resize((400, 300))
        img.save(os.path.join(save_dir, filename))
        return True
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        return False

# Create directories
base_dir = "test_images"

test_sets = {
    "cats_with_dog": {
        "main": "british_shorthair",
        "intruder": "labrador",
        "urls": {
            "british_shorthair": [
                # Placeholder images from public sources
                "https://picsum.photos/seed/british1/400/300",
                "https://picsum.photos/seed/british2/400/300",
                "https://picsum.photos/seed/british3/400/300",
                "https://picsum.photos/seed/british4/400/300",
                "https://picsum.photos/seed/british5/400/300",
                "https://picsum.photos/seed/british6/400/300",
                "https://picsum.photos/seed/british7/400/300",
                "https://picsum.photos/seed/british8/400/300",
            ],
            "labrador": [
                "https://picsum.photos/seed/labrador1/400/300"
            ]
        }
    },
    "dogs_with_cat": {
        "main": "labrador",
        "intruder": "british_shorthair",
        "urls": {
            "labrador": [
                "https://picsum.photos/seed/labrador2/400/300",
                "https://picsum.photos/seed/labrador3/400/300",
                "https://picsum.photos/seed/labrador4/400/300",
                "https://picsum.photos/seed/labrador5/400/300",
                "https://picsum.photos/seed/labrador6/400/300",
                "https://picsum.photos/seed/labrador7/400/300",
                "https://picsum.photos/seed/labrador8/400/300",
                "https://picsum.photos/seed/labrador9/400/300",
            ],
            "british_shorthair": [
                "https://picsum.photos/seed/british9/400/300"
            ]
        }
    },
    "cars_with_tree": {
        "main": "car",
        "intruder": "tree",
        "urls": {
            "car": [
                "https://picsum.photos/seed/car1/400/300",
                "https://picsum.photos/seed/car2/400/300",
                "https://picsum.photos/seed/car3/400/300",
                "https://picsum.photos/seed/car4/400/300",
                "https://picsum.photos/seed/car5/400/300",
                "https://picsum.photos/seed/car6/400/300",
                "https://picsum.photos/seed/car7/400/300",
                "https://picsum.photos/seed/car8/400/300",
            ],
            "tree": [
                "https://picsum.photos/seed/tree1/400/300"
            ]
        }
    },
    "trees_with_car": {
        "main": "tree",
        "intruder": "car",
        "urls": {
            "tree": [
                "https://picsum.photos/seed/tree2/400/300",
                "https://picsum.photos/seed/tree3/400/300",
                "https://picsum.photos/seed/tree4/400/300",
                "https://picsum.photos/seed/tree5/400/300",
                "https://picsum.photos/seed/tree6/400/300",
                "https://picsum.photos/seed/tree7/400/300",
                "https://picsum.photos/seed/tree8/400/300",
                "https://picsum.photos/seed/tree9/400/300",
            ],
            "car": [
                "https://picsum.photos/seed/car9/400/300"
            ]
        }
    }
}

# Process each test set
for test_set_name, data in test_sets.items():
    test_dir = os.path.join(base_dir, test_set_name)
    
    # Clear if exists
    if os.path.exists(test_dir):
        import shutil
        shutil.rmtree(test_dir)
    os.makedirs(test_dir, exist_ok=True)
    
    print(f"\nCreating test set: {test_set_name}")
    
    # Download main object images
    for i, url in enumerate(data["urls"][data["main"]]):
        filename = f"{data['main']}_{i:02d}.png"
        if download_image(url, filename, test_dir):
            print(f"  - {filename}")
    
    # Download intruder image
    intruder_url = data["urls"][data["intruder"]][0]
    intruder_filename = f"{data['intruder']}_intruder.png"
    if download_image(intruder_url, intruder_filename, test_dir):
        print(f"  - {intruder_filename} (INTRUDER)")

print("\nTest sets created with real images!")
