
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

<a name="english"></a>

## English

### 🌟 Features

- **Pure Hard-Coded** - No AI/ML dependencies
- **Zero-Shot Learning** - Works with any image out of the box
- **Scale Invariant** - Handle different zoom levels (0.5x to 2x)
- **Rotation Invariant** - Support 0-360 degree rotation
- **Brightness Tolerant** - Works with different lighting conditions
- **Noise Robust** - Handles image noise
- **Cropping Robust** - Compare partial to full images

### 📊 Demo Results

#### 1. Same Object Transformations (High Similarity)

Image Pair | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC | Description
--- | --- | --- | --- | --- | --- | --- | ---
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![Scaled 0.75x](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/scale_0.75.png) | **98.9%** | 99.2% | 98.8% | 98.5% | 99.5% | 99.5% | Scale 0.75x
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![Rotated 90°](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/rotate_090.png) | **94.4%** | 99.5% | 95.2% | 89.6% | 92.1% | 98.5% | Rotate 90°
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![Rotated 180°](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/rotate_180.png) | **92.6%** | 99.3% | 94.8% | 88.2% | 91.5% | 98.3% | Rotate 180°
![Original](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![Cropped](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/crop_01.png) | **68.2%** | 92.1% | 72.5% | 55.3% | 49.6% | 52.3% | Partial Crop

#### 2. Same Color Bubbles (High Similarity)

Bubble Pair | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC | Description
--- | --- | --- | --- | --- | --- | --- | ---
![Yellow 00](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) + ![Yellow 01](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_01.png) | **86.0%** | 99.9% | 100.0% | 84.9% | 65.0% | 67.2% | Same Color, Different Variation
![Yellow 00](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) + ![Yellow 02](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_02.png) | **85.1%** | 99.7% | 99.5% | 83.2% | 62.8% | 65.4% | Same Color, Different Variation

#### 3. Different Objects (Low Similarity)

Image Pair | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC | Description
--- | --- | --- | --- | --- | --- | --- | ---
![Yellow Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) + ![Blue Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/blue_bubble_intruder.png) | **40.2%** | 0.0% | 45.8% | 70.6% | 38.6% | 38.6% | Different Colors
![Green Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/green_with_red/green_bubble_00.png) + ![Red Bubble](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/green_with_red/red_bubble_intruder.png) | **45.6%** | 0.2% | 52.1% | 74.2% | 41.5% | 41.5% | Different Colors

### 🧠 Algorithm Overview

This system combines **5 different techniques** for robust image comparison:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Histogram Similarity** | 25% | Compares pixel intensity distributions |
| **Feature Comparison** | 20% | Compares statistical features and gradient features |
| **SSIM (Structural Similarity)** | 25% | Measures structural similarity with rotation alignment |
| **NCC (Normalized Cross-Correlation)** | 15% | Template matching with rotation alignment |
| **Rotated NCC** | 15% | Best NCC score after trying multiple rotations |

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

### 🌟 功能特性

- **纯硬编码** - 无 AI/ML 依赖
- **零样本识别** - 开箱即用，适用于任何图像
- **缩放不变性** - 处理不同放大倍数（0.5x 至 2x）
- **旋转不变性** - 支持 0-360 度旋转
- **亮度容忍** - 适应不同光照条件
- **噪声鲁棒** - 处理图像噪声
- **裁剪鲁棒** - 比较局部与完整图像

### 📊 演示结果

#### 1. 相同物体变换（高相似度）

图像对 | 相似度 | 直方图相似度 | 特征比较 | SSIM | NCC | 旋转对齐 NCC | 说明
--- | --- | --- | --- | --- | --- | --- | ---
![原图](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![缩放 0.75x](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/scale_0.75.png) | **98.9%** | 99.2% | 98.8% | 98.5% | 99.5% | 99.5% | 缩放 0.75 倍
![原图](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![旋转 90°](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/rotate_090.png) | **94.4%** | 99.5% | 95.2% | 89.6% | 92.1% | 98.5% | 旋转 90 度
![原图](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![旋转 180°](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/rotate_180.png) | **92.6%** | 99.3% | 94.8% | 88.2% | 91.5% | 98.3% | 旋转 180 度
![原图](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/original.png) + ![裁剪](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/small_test/crop_01.png) | **68.2%** | 92.1% | 72.5% | 55.3% | 49.6% | 52.3% | 局部裁剪

#### 2. 相同颜色泡泡（高相似度）

泡泡对 | 相似度 | 直方图相似度 | 特征比较 | SSIM | NCC | 旋转对齐 NCC | 说明
--- | --- | --- | --- | --- | --- | --- | ---
![黄色 00](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) + ![黄色 01](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_01.png) | **86.0%** | 99.9% | 100.0% | 84.9% | 65.0% | 67.2% | 相同颜色，不同变体
![黄色 00](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) + ![黄色 02](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_02.png) | **85.1%** | 99.7% | 99.5% | 83.2% | 62.8% | 65.4% | 相同颜色，不同变体

#### 3. 不同物体（低相似度）

图像对 | 相似度 | 直方图相似度 | 特征比较 | SSIM | NCC | 旋转对齐 NCC | 说明
--- | --- | --- | --- | --- | --- | --- | ---
![黄色泡泡](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/yellow_bubble_00.png) + ![蓝色泡泡](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/yellow_with_blue/blue_bubble_intruder.png) | **40.2%** | 0.0% | 45.8% | 70.6% | 38.6% | 38.6% | 不同颜色
![绿色泡泡](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/green_with_red/green_bubble_00.png) + ![红色泡泡](https://raw.githubusercontent.com/LAlfredX/NoAIMatch/main/test_images/green_with_red/red_bubble_intruder.png) | **45.6%** | 0.2% | 52.1% | 74.2% | 41.5% | 41.5% | 不同颜色

### 🧠 算法概述

本系统结合 **5 种不同技术** 进行鲁棒的图像比对：

| 因素 | 权重 | 说明 |
|--------|--------|-------------|
| **直方图相似度** | 25% | 比较像素强度分布 |
| **特征比较** | 20% | 比较统计特征和梯度特征 |
| **SSIM (结构相似性)** | 25% | 测量结构相似性（带旋转对齐） |
| **NCC (归一化互相关)** | 15% | 模板匹配（带旋转对齐） |
| **旋转对齐 NCC** | 15% | 尝试多个旋转后的最佳 NCC 分数 |

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

## 🤝 Contributing / 贡献

Contributions are welcome! Please feel free to submit issues and pull requests.

欢迎贡献！请随时提交 Issue 和 Pull Request。

## ⭐ Star History

If you find this project useful, please give it a star! ⭐

如果觉得这个项目有用，请给颗星！⭐

---

Made with ❤️ by [LAlfredX](https://github.com/LAlfredX)

