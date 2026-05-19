
# NoAIMatch

100% pure hard-coded image similarity comparison - No AI, No ML, Just Math!

---

[English](#english) | [中文](#chinese)

---

&lt;a name="english"&gt;&lt;/a&gt;

## English

### What is NoAIMatch?

NoAIMatch is a 100% pure hard-coded image similarity comparison system! No AI, no neural networks, no machine learning - just pure mathematics and algorithms.

Zero-shot learning, works with any image out of the box!

### Algorithm Overview

This system combines 5 different techniques for robust image comparison:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Histogram Similarity** | 25% | Compares pixel intensity distributions |
| **Feature Comparison** | 20% | Compares statistical features and gradient features |
| **SSIM (Structural Similarity)** | 25% | Measures structural similarity with rotation alignment |
| **NCC (Normalized Cross-Correlation)** | 15% | Template matching with rotation alignment |
| **Rotated NCC** | 15% | Best NCC score after trying multiple rotations |

### Features

- Pure Hard-Coded - No AI/ML dependencies
- Zero-Shot Learning - Works with any image
- Scale Invariant - Handle different zoom levels
- Rotation Invariant - Support 0-360 degree rotation
- Brightness Tolerant - Works with different lighting
- Noise Robust - Handles image noise
- Cropping Robust - Compare partial to full images

### Demo Results

#### Similar Images (High Similarity)

| Image 1 | Image 2 | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC |
|---------|---------|------------|-----------|----------|------|-----|-------------|
| Yellow Bubble 00 | Yellow Bubble 01 | 86.0% | 99.9% | 100.0% | 84.9% | 65.0% | 67.2% |
| Yellow Bubble 01 | Yellow Bubble 02 | 87.4% | 97.7% | 99.3% | 83.9% | 72.7% | 75.1% |
| Yellow Bubble 02 | Yellow Bubble 03 | 88.6% | 100.0% | 99.8% | 86.7% | 73.3% | 73.3% |

#### Different Images (Low Similarity)

| Image 1 | Image 2 | Similarity | Histogram | Features | SSIM | NCC | Rotated NCC |
|---------|---------|------------|-----------|----------|------|-----|-------------|
| Yellow Bubble | Blue Bubble | 40.2% | 0.0% | 45.8% | 70.6% | 38.6% | 38.6% |
| Yellow Bubble | Blue Bubble | 41.7% | 0.0% | 58.6% | 71.8% | 40.1% | 40.1% |

### Quick Start

```bash
# Clone or download this project
cd FrechetDistance

# Install dependencies
pip install -r requirements.txt

# Interactive mode
python main.py

# Or use command line
python main.py -l
python main.py -t yellow_with_blue
```

### Project Structure

```
FrechetDistance/
├── main.py
├── image_processor.py
├── requirements.txt
└── test_images/
    ├── small_test/
    ├── transform_test/
    ├── yellow_with_blue/
    ├── blue_with_yellow/
    ├── green_with_red/
    └── red_with_green/
```

### License

MIT License

---

&lt;a name="chinese"&gt;&lt;/a&gt;

## 中文

### 什么是 NoAIMatch？

NoAIMatch 是一个 100% 纯硬编码的图像相似度比对系统！没有 AI、没有神经网络、没有机器学习 - 只靠纯粹的数学和算法！

零样本识别，开箱即用，适用于任何图像！

### 算法原理

这个系统结合了 5 种技术进行鲁棒的图像比对：

| 因素 | 权重 | 说明 |
|------|------|------|
| **直方图相似度** | 25% | 比较像素强度分布 |
| **特征比较** | 20% | 比较统计特征和梯度特征 |
| **SSIM (结构相似性)** | 25% | 带有旋转对齐的结构相似性测量 |
| **NCC (归一化互相关)** | 15% | 带有旋转对齐的模板匹配 |
| **旋转对齐 NCC** | 15% | 尝试多个旋转后的最佳 NCC 分数 |

### 特性

- 纯硬编码 - 无 AI/ML 依赖
- 零样本识别 - 适用于任何图像
- 缩放不变性 - 处理不同放大倍数
- 旋转不变性 - 支持 0-360 度旋转
- 亮度容忍 - 适应不同光照条件
- 噪声鲁棒 - 处理图像噪声
- 裁剪鲁棒 - 比较局部和完整图像

### 演示效果

#### 相似图片（高相似度）

| 图片1 | 图片2 | 相似度 | 直方图 | 特征 | SSIM | NCC | 旋转NCC |
|-------|-------|--------|--------|------|------|-----|---------|
| 黄色泡泡00 | 黄色泡泡01 | 86.0% | 99.9% | 100.0% | 84.9% | 65.0% | 67.2% |
| 黄色泡泡01 | 黄色泡泡02 | 87.4% | 97.7% | 99.3% | 83.9% | 72.7% | 75.1% |
| 黄色泡泡02 | 黄色泡泡03 | 88.6% | 100.0% | 99.8% | 86.7% | 73.3% | 73.3% |

#### 不同图片（低相似度）

| 图片1 | 图片2 | 相似度 | 直方图 | 特征 | SSIM | NCC | 旋转NCC |
|-------|-------|--------|--------|------|------|-----|---------|
| 黄色泡泡 | 蓝色泡泡 | 40.2% | 0.0% | 45.8% | 70.6% | 38.6% | 38.6% |
| 黄色泡泡 | 蓝色泡泡 | 41.7% | 0.0% | 58.6% | 71.8% | 40.1% | 40.1% |

### 快速开始

```bash
# 克隆或下载项目
cd FrechetDistance

# 安装依赖
pip install -r requirements.txt

# 交互模式
python main.py

# 或使用命令行
python main.py -l
python main.py -t yellow_with_blue
```

### 项目结构

```
FrechetDistance/
├── main.py
├── image_processor.py
├── requirements.txt
└── test_images/
    ├── small_test/
    ├── transform_test/
    ├── yellow_with_blue/
    ├── blue_with_yellow/
    ├── green_with_red/
    └── red_with_green/
```

### 许可证

MIT License

---

If you find this useful, give it a star!
如果觉得有用，给个星星支持一下！

