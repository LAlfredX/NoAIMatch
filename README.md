
# NoAIMatch

100% pure hard-coded image similarity comparison - No AI, No ML, Just Math!

---

[English](#english) | [中文](#chinese)

---

<a name="english"></a>

## English

### What is NoAIMatch?

NoAIMatch is a 100% pure hard-coded image similarity comparison system! No AI, no neural networks, no machine learning - just pure mathematics and algorithms.

Zero-shot learning, works with any image out of the box!

### Algorithm Overview

This system combines 5 different techniques for robust image comparison:

1. Histogram Similarity - Compares pixel intensity distributions
2. Feature Comparison - Compares statistical features and gradient features
3. SSIM - Measures structural similarity with rotation alignment
4. NCC - Template matching with rotation alignment
5. Weighted Fusion - Intelligently combines all 4 methods

### Features

- Pure Hard-Coded - No AI/ML dependencies
- Zero-Shot Learning - Works with any image
- Scale Invariant - Handle different zoom levels
- Rotation Invariant - Support 0-360 degree rotation
- Brightness Tolerant - Works with different lighting
- Noise Robust - Handles image noise
- Cropping Robust - Compare partial to full images

### Demo Results

| Transformation | Similarity |
|----------------|------------|
| Scale 0.75x | 98.9% |
| Rotate 90 degree | 94.4% |
| Rotate 180 degree | 92.6% |
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
python main.py -l
python main.py -t small_test
```

### Project Structure

```
FrechetDistance/
├── main.py
├── image_processor.py
├── requirements.txt
└── test_images/
    ├── small_test/
    └── transform_test/
```

### License

MIT License

---

<a name="chinese"></a>

## 中文

### 什么是 NoAIMatch？

NoAIMatch 是一个 100% 纯硬编码的图像相似度比对系统！没有 AI、没有神经网络、没有机器学习 - 只靠纯粹的数学和算法！

零样本识别，开箱即用，适用于任何图像！

### 算法原理

这个系统结合了 5 种技术进行鲁棒的图像比对：

1. 直方图相似度 - 比较像素强度分布
2. 特征比较 - 比较统计特征和梯度特征
3. SSIM - 带有旋转对齐的结构相似性测量
4. NCC - 带有旋转对齐的模板匹配
5. 加权融合 - 智能融合以上 4 种方法

### 特性

- 纯硬编码 - 无 AI/ML 依赖
- 零样本识别 - 适用于任何图像
- 缩放不变性 - 处理不同放大倍数
- 旋转不变性 - 支持 0-360 度旋转
- 亮度容忍 - 适应不同光照条件
- 噪声鲁棒 - 处理图像噪声
- 裁剪鲁棒 - 比较局部和完整图像

### 演示效果

| 变换类型 | 相似度 |
|----------|---------|
| 缩放 0.75 倍 | 98.9% |
| 旋转 90 度 | 94.4% |
| 旋转 180 度 | 92.6% |
| 裁剪（局部） | 68.2% |

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
python main.py -t small_test
```

### 项目结构

```
FrechetDistance/
├── main.py
├── image_processor.py
├── requirements.txt
└── test_images/
    ├── small_test/
    └── transform_test/
```

### 许可证

MIT License

---

If you find this useful, give it a star!
如果觉得有用，给个星星支持一下！
