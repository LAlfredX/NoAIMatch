
&lt;div align="center"&gt;

# 🔍 Pure Hard-Coded Image Similarity Comparison
# 🔍 纯硬编码图像相似度比对

&lt;/div&gt;

&lt;br&gt;

&lt;p align="center"&gt;
  &lt;a href="#english"&gt;English&lt;/a&gt; •
  &lt;a href="#chinese"&gt;中文&lt;/a&gt;
&lt;/p&gt;

&lt;br&gt;

---

&lt;a name="english"&gt;&lt;/a&gt;
## 🇬🇧 English

### 🎯 What is this?

A **100% pure hard-coded** image similarity comparison system! **No AI, no neural networks, no machine learning** — just pure mathematics and algorithms.

### 🧠 Algorithm Overview

This system combines 5 different techniques for robust image comparison:

1. **Histogram Similarity** - Compares pixel intensity distributions (invariant to rotation and scale)
2. **Feature Comparison** - Compares statistical features (mean, standard deviation) and gradient features
3. **SSIM (Structural Similarity Index)** - Measures structural similarity with rotation alignment
4. **NCC (Normalized Cross-Correlation)** - Template matching with rotation alignment
5. **Weighted Fusion** - Intelligently combines all 4 methods with optimal weights

### ✨ Features

- ✅ **Pure Hard-Coded** - No AI/ML dependencies
- ✅ **Zero-Shot Learning** - Works with any image out of the box
- ✅ **Scale Invariant** - Handle different zoom levels
- ✅ **Rotation Invariant** - Support 0-360° rotation
- ✅ **Brightness Tolerant** - Works with different lighting
- ✅ **Noise Robust** - Handles image noise
- ✅ **Cropping Robust** - Compare partial to full images

### 📊 Demo Results

| Transformation | Image 1 | Image 2 | Similarity |
|----------------|---------|---------|------------|
| Scale 0.75x | ![Original](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![Scaled](https://via.placeholder.com/100x100/10b981/ffffff?text=0.75x) | **98.9%** 🔥 |
| Rotate 90° | ![Original](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![Rotated](https://via.placeholder.com/100x100/f59e0b/ffffff?text=90°) | **94.4%** 🔥 |
| Rotate 180° | ![Original](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![Rotated](https://via.placeholder.com/100x100/ef4444/ffffff?text=180°) | **92.6%** 🔥 |
| Crop (Partial) | ![Original](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![Cropped](https://via.placeholder.com/100x100/8b5cf6/ffffff?text=CROP) | **68.2%** ✨ |

### 🚀 Quick Start

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

### 📁 Project Structure

```
FrechetDistance/
├── main.py                    # Main program (CLI & Interactive)
├── image_processor.py         # Core algorithm (V3 Optimized)
├── requirements.txt           # Dependencies
└── test_images/              # Test image sets
    ├── small_test/
    └── transform_test/
```

### 📝 License

MIT License - Use it for anything!

---

&lt;a name="chinese"&gt;&lt;/a&gt;
## 🇨🇳 中文

### 🎯 这是什么？

一个**100%纯硬编码**的图像相似度比对系统！**没有AI、没有神经网络、没有机器学习** —— 只靠纯粹的数学和算法！

### 🧠 算法原理

这个系统结合了5种先进技术进行鲁棒的图像比对：

1. **直方图相似度** - 比较像素强度分布（对旋转和缩放不变）
2. **特征比较** - 比较统计特征（均值、标准差）和梯度特征
3. **SSIM（结构相似性指数）** - 带有旋转对齐的结构相似性测量
4. **NCC（归一化互相关）** - 带有旋转对齐的模板匹配
5. **加权融合** - 使用最优权重智能融合以上4种方法

### ✨ 特性

- ✅ **纯硬编码** - 无任何AI/ML依赖
- ✅ **零样本识别** - 开箱即用，适用于任何图片
- ✅ **缩放不变性** - 处理不同的放大倍数
- ✅ **旋转不变性** - 支持0-360°任意旋转
- ✅ **亮度容忍** - 适应不同光照条件
- ✅ **噪声鲁棒** - 处理图像噪声
- ✅ **裁剪鲁棒** - 比较局部和完整图片

### 📊 演示效果

| 变换类型 | 图片1 | 图片2 | 相似度 |
|----------|--------|--------|---------|
| 缩放0.75倍 | ![原图](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![缩放](https://via.placeholder.com/100x100/10b981/ffffff?text=0.75x) | **98.9%** 🔥 |
| 旋转90度 | ![原图](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![旋转](https://via.placeholder.com/100x100/f59e0b/ffffff?text=90°) | **94.4%** 🔥 |
| 旋转180度 | ![原图](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![旋转](https://via.placeholder.com/100x100/ef4444/ffffff?text=180°) | **92.6%** 🔥 |
| 裁剪（局部） | ![原图](https://via.placeholder.com/100x100/3b82f6/ffffff?text=ORIG) | ![裁剪](https://via.placeholder.com/100x100/8b5cf6/ffffff?text=CROP) | **68.2%** ✨ |

### 🚀 快速开始

```bash
# 克隆或下载项目
cd FrechetDistance

# 安装依赖
pip install -r requirements.txt

# 交互模式
python main.py

# 或使用命令行
python main.py -l                       # 列出测试集
python main.py -t small_test            # 运行比较
```

### 📁 项目结构

```
FrechetDistance/
├── main.py                    # 主程序（命令行 & 交互式）
├── image_processor.py         # 核心算法（V3优化版）
├── requirements.txt           # 依赖库
└── test_images/              # 测试图片集
    ├── small_test/
    └── transform_test/
```

### 📝 许可证

MIT License - 任意使用！

&lt;br&gt;

---

&lt;div align="center"&gt;

**⭐ If you find this useful, give it a star!**  
**⭐ 如果觉得有用，给个星星支持一下！**

&lt;/div&gt;
