# NoAIMatch

100% pure hard-coded image similarity comparison — No AI, No ML, Just Math!

---

### What is NoAIMatch?

NoAIMatch is a 100% pure hard-coded image similarity comparison system! No AI, no neural networks, no machine learning — just pure mathematics and algorithms.

> Zero-shot learning, works with any image out of the box!

### Algorithm Overview

This system combines 5 different techniques for robust image comparison:

1. **Histogram Similarity** - Compares pixel intensity distributions (invariant to rotation and scale)
2. **Feature Comparison** - Compares statistical features (mean, standard deviation) and gradient features
3. **SSIM (Structural Similarity Index)** - Measures structural similarity with rotation alignment
4. **NCC (Normalized Cross-Correlation)** - Template matching with rotation alignment
5. **Weighted Fusion** - Intelligently combines all 4 methods with optimal weights

### Features

- **Pure Hard-Coded** - No AI/ML dependencies
- **Zero-Shot Learning** - Works with any image out of the box
- **Scale Invariant** - Handle different zoom levels
- **Rotation Invariant** - Support 0-360° rotation
- **Brightness Tolerant** - Works with different lighting
- **Noise Robust** - Handles image noise
- **Cropping Robust** - Compare partial to full images

### Demo Results

| Transformation | Similarity |
|----------------|------------|
| Scale 0.75x | 98.9% |
| Rotate 90° | 94.4% |
| Rotate 180° | 92.6% |
| Crop (Partial) | 68.2% |

### Quick Start

```bash
# Clone or download this project
cd FrechetDistance

# Install dependencies
pip install -r requirements.txt

# Interactive mode
python main.py

# Or use command line
python main.py -l                       # List test sets
python main.py -t small_test            # Run comparison
```

### Project Structure

```
FrechetDistance/
├── main.py                    # Main program (CLI & Interactive)
├── image_processor.py         # Core algorithm (V3 Optimized)
├── requirements.txt           # Dependencies
└── test_images/              # Test image sets
    ├── small_test/
    └── transform_test/
```

### License

MIT License - Use it for anything!

