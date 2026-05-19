
# NoAIMatch

<p align="center">
  <img src="https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/docs/demo_banner.png" alt="NoAIMatch Banner" width="600"/>
</p>

**100% pure hard-coded image similarity comparison** - No AI, No ML, Just Math!

---

<p align="center">
  <a href="#english">English</a> | <a href="#chinese">中文</a>
</p>

---

## 🌟 Features

- **Pure Hard-Coded** - No AI/ML dependencies
- **Zero-Shot Learning** - Works with any image out of the box
- **Scale Invariant** - Handle different zoom levels (0.5x to 2x)
- **Rotation Invariant** - Support 0-360 degree rotation
- **Brightness Tolerant** - Works with different lighting conditions
- **Noise Robust** - Handles image noise
- **Cropping Robust** - Compare partial to full images

---

## 📊 Demo Results

### Similar Images (High Similarity)

Original Image | Transformed Image | Similarity Score | Description
--- | --- | --- | ---
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) | ![Scaled 0.75x](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/scale_0.75.png) | **98.9%** | Scale 0.75x
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) | ![Rotated 90°](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/rotate_090.png) | **94.4%** | Rotate 90°
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) | ![Rotated 180°](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/rotate_180.png) | **92.6%** | Rotate 180°
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) | ![Cropped](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/crop_01.png) | **68.2%** | Partial Crop

### Different Images (Low Similarity)

Image 1 | Image 2 | Similarity Score | Description
--- | --- | --- | ---
![Yellow Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) | ![Blue Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/blue_bubble_intruder.png) | **40.2%** | Different Colors
![Green Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/green_with_red/green_bubble_00.png) | ![Red Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/green_with_red/red_bubble_intruder.png) | **45.6%** | Different Colors

---

## 🧠 Algorithm Overview

This system combines **5 different techniques** for robust image comparison:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Histogram Similarity** | 25% | Compares pixel intensity distributions |
| **Feature Comparison** | 20% | Compares statistical features and gradient features |
| **SSIM (Structural Similarity)** | 25% | Measures structural similarity with rotation alignment |
| **NCC (Normalized Cross-Correlation)** | 15% | Template matching with rotation alignment |
| **Rotated NCC** | 15% | Best NCC score after trying multiple rotations |

### Factor Breakdown Analysis

#### Similar Images (Yellow Bubbles)

| Image Pair | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC |
|------------|------------|-----------|----------|------|-----|-------------|
| Yellow 00 vs Yellow 01 | 86.0% | 99.9% | 100.0% | 84.9% | 65.0% | 67.2% |
| Yellow 01 vs Yellow 02 | 87.4% | 97.7% | 99.3% | 83.9% | 72.7% | 75.1% |
| Yellow 02 vs Yellow 03 | 88.6% | 100.0% | 99.8% | 86.7% | 73.3% | 73.3% |

#### Different Images (Yellow vs Blue)

| Image Pair | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC |
|------------|------------|-----------|----------|------|-----|-------------|
| Yellow vs Blue | 40.2% | 0.0% | 45.8% | 70.6% | 38.6% | 38.6% |
| Yellow vs Blue | 41.7% | 0.0% | 58.6% | 71.8% | 40.1% | 40.1% |

---

<a name="english"></a>

## English

### What is NoAIMatch?

NoAIMatch is a **100% pure hard-coded image similarity comparison system**! No AI, no neural networks, no machine learning - just pure mathematics and algorithms.

Zero-shot learning, works with any image out of the box!

### Quick Start

```bash
# Clone this repository
git clone https://github.com/LAlfredX/NoAIMatch.git
cd NoAIMatch

# Install dependencies
pip install -r requirements.txt

# Run in interactive mode
python main.py

# Run specific test set
python main.py -t small_test
```

### Command Line Usage

```bash
# List available test sets
python main.py -l

# Run comparison on specific test set
python main.py -t yellow_with_blue

# Create new test set
python main.py -c my_new_set

# Run without saving log file
python main.py -t small_test -n
```

### Project Structure

```
NoAIMatch/
├── main.py              # Main entry point (CLI + Interactive)
├── image_processor.py   # Core algorithm implementation
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── test_images/         # Test image datasets
    ├── small_test/      # Basic transformation tests
    ├── transform_test/  # Comprehensive transformation tests
    ├── yellow_with_blue/# Color-based similarity tests
    ├── blue_with_yellow/
    ├── green_with_red/
    └── red_with_green/
```

### License

MIT License

---

<a name="chinese"></a>

## 中文

### 什么是 NoAIMatch？

NoAIMatch 是一个 **100% 纯硬编码的图像相似度比对系统**！没有 AI、没有神经网络、没有机器学习 - 只靠纯粹的数学和算法！

零样本识别，开箱即用，适用于任何图像！

### 快速开始

```bash
# 克隆仓库
git clone https://github.com/LAlfredX/NoAIMatch.git
cd NoAIMatch

# 安装依赖
pip install -r requirements.txt

# 运行交互模式
python main.py

# 运行指定测试集
python main.py -t small_test
```

### 命令行用法

```bash
# 列出可用测试集
python main.py -l

# 在指定测试集上运行比较
python main.py -t yellow_with_blue

# 创建新测试集
python main.py -c my_new_set

# 运行不保存日志
python main.py -t small_test -n
```

### 项目结构

```
NoAIMatch/
├── main.py              # 主入口（命令行 + 交互模式）
├── image_processor.py   # 核心算法实现
├── requirements.txt     # 依赖库
├── README.md            # 文档
└── test_images/         # 测试图片数据集
    ├── small_test/      # 基础变换测试
    ├── transform_test/  # 综合变换测试
    ├── yellow_with_blue/# 颜色相似度测试
    ├── blue_with_yellow/
    ├── green_with_red/
    └── red_with_green/
```

### 许可证

MIT License

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## ⭐ Star History

If you find this project useful, please give it a star! ⭐

---

Made with ❤️ by [LAlfredX](https://github.com/LAlfredX)

