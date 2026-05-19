import numpy as np
from PIL import Image
import math


def load_image(image_path, grayscale=False):
    img = Image.open(image_path)
    if grayscale:
        img = img.convert('L')
    else:
        img = img.convert('RGB')
    return np.array(img, dtype=np.float64)


def normalize_pixel_values(image):
    return image / 255.0


def to_grayscale(image):
    if image.ndim == 3:
        return 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 2]
    return image


def resize_to_match(img1, img2, target_size=None):
    """将两张图调整到相同尺寸"""
    if target_size is None:
        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]
        new_h = min(h1, h2)
        new_w = min(w1, w2)
    else:
        new_h, new_w = target_size
    
    if img1.ndim == 3:
        img1_pil = Image.fromarray((img1 * 255).astype(np.uint8))
        img1_resized = np.array(img1_pil.resize((new_w, new_h), Image.LANCZOS)) / 255.0
    else:
        img1_pil = Image.fromarray((img1 * 255).astype(np.uint8))
        img1_resized = np.array(img1_pil.resize((new_w, new_h), Image.LANCZOS)) / 255.0
    
    if img2.ndim == 3:
        img2_pil = Image.fromarray((img2 * 255).astype(np.uint8))
        img2_resized = np.array(img2_pil.resize((new_w, new_h), Image.LANCZOS)) / 255.0
    else:
        img2_pil = Image.fromarray((img2 * 255).astype(np.uint8))
        img2_resized = np.array(img2_pil.resize((new_w, new_h), Image.LANCZOS)) / 255.0
    
    return img1_resized, img2_resized


def rotate_image_array(img, angle):
    """旋转numpy数组"""
    h, w = img.shape[:2]
    center = (w / 2, h / 2)
    
    if img.ndim == 3:
        pil_img = Image.fromarray((img * 255).astype(np.uint8))
    else:
        pil_img = Image.fromarray((img * 255).astype(np.uint8))
    
    rotated = pil_img.rotate(angle, expand=True, resample=Image.BICUBIC)
    rotated_np = np.array(rotated) / 255.0
    
    new_h, new_w = rotated_np.shape[:2]
    start_h = (new_h - h) // 2
    start_w = (new_w - w) // 2
    return rotated_np[start_h:start_h+h, start_w:start_w+w]


def calculate_histogram(image, bins=32):
    """计算灰度直方图"""
    if image.ndim == 3:
        image = to_grayscale(image)
    
    hist, _ = np.histogram(image.flatten(), bins=bins, range=(0, 1))
    hist = hist / np.sum(hist)
    return hist


def histogram_intersection(hist1, hist2):
    """直方图相交相似度"""
    return np.sum(np.minimum(hist1, hist2))


def calculate_ssim(img1, img2, window_size=11, K1=0.01, K2=0.03):
    """计算结构相似性指数 (SSIM)"""
    if img1.ndim == 3:
        img1 = to_grayscale(img1)
    if img2.ndim == 3:
        img2 = to_grayscale(img2)
    
    img1, img2 = resize_to_match(img1, img2)
    
    C1 = (K1 * 1) ** 2
    C2 = (K2 * 1) ** 2
    
    h, w = img1.shape
    num_blocks_y = max(1, h // window_size)
    num_blocks_x = max(1, w // window_size)
    
    ssim_values = []
    
    for i in range(num_blocks_y):
        for j in range(num_blocks_x):
            y_start = i * window_size
            y_end = min(y_start + window_size, h)
            x_start = j * window_size
            x_end = min(x_start + window_size, w)
            
            block1 = img1[y_start:y_end, x_start:x_end]
            block2 = img2[y_start:y_end, x_start:x_end]
            
            mu1 = np.mean(block1)
            mu2 = np.mean(block2)
            sigma1 = np.var(block1)
            sigma2 = np.var(block2)
            sigma12 = np.mean((block1 - mu1) * (block2 - mu2))
            
            ssim = ((2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)) / ((mu1**2 + mu2**2 + C1) * (sigma1 + sigma2 + C2))
            ssim_values.append(ssim)
    
    return np.mean(ssim_values)


def calculate_ncc(img1, img2):
    """归一化互相关"""
    if img1.ndim == 3:
        img1 = to_grayscale(img1)
    if img2.ndim == 3:
        img2 = to_grayscale(img2)
    
    img1, img2 = resize_to_match(img1, img2)
    
    mean1 = np.mean(img1)
    mean2 = np.mean(img2)
    
    img1_centered = img1 - mean1
    img2_centered = img2 - mean2
    
    numerator = np.sum(img1_centered * img2_centered)
    denominator = np.sqrt(np.sum(img1_centered**2) * np.sum(img2_centered**2))
    
    if denominator == 0:
        return 0.0
    
    return (numerator / denominator + 1) / 2


def extract_features(image):
    """提取多种特征"""
    features = {}
    
    if image.ndim == 3:
        gray = to_grayscale(image)
    else:
        gray = image
    
    features['mean'] = np.mean(gray)
    features['std'] = np.std(gray)
    
    grad_x = np.zeros_like(gray)
    grad_y = np.zeros_like(gray)
    
    grad_x[:, 1:-1] = (gray[:, 2:] - gray[:, :-2]) / 2.0
    grad_y[1:-1, :] = (gray[2:, :] - gray[:-2, :]) / 2.0
    
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)
    features['grad_mean'] = np.mean(grad_mag)
    features['grad_std'] = np.std(grad_mag)
    
    features['histogram'] = calculate_histogram(gray, bins=16)
    
    return features


def compare_features(feat1, feat2):
    """比较特征相似度"""
    scores = []
    
    mean_diff = abs(feat1['mean'] - feat2['mean'])
    std_diff = abs(feat1['std'] - feat2['std'])
    scores.append(1.0 - min(1.0, mean_diff * 3.0))
    scores.append(1.0 - min(1.0, std_diff * 3.0))
    
    grad_mean_diff = abs(feat1['grad_mean'] - feat2['grad_mean'])
    grad_std_diff = abs(feat1['grad_std'] - feat2['grad_std'])
    scores.append(1.0 - min(1.0, grad_mean_diff * 4.0))
    scores.append(1.0 - min(1.0, grad_std_diff * 4.0))
    
    hist_sim = histogram_intersection(feat1['histogram'], feat2['histogram'])
    scores.append(hist_sim)
    
    return np.mean(scores)


def find_best_rotation(img1, img2):
    """尝试不同的旋转角度，找到最佳匹配"""
    if img1.ndim == 3:
        img1_gray = to_grayscale(img1)
    else:
        img1_gray = img1
    
    if img2.ndim == 3:
        img2_gray = to_grayscale(img2)
    else:
        img2_gray = img2
    
    best_score = 0
    best_angle = 0
    
    angles = [0, 90, 180, 270, 45, 135, 225, 315]
    
    for angle in angles:
        rotated = rotate_image_array(img2_gray, angle)
        score = calculate_ssim(img1_gray, rotated)
        
        if score > best_score:
            best_score = score
            best_angle = angle
    
    return best_angle, best_score


def compare_images(image_path1, image_path2, return_intermediate=False):
    """
    综合相似度比较 - 最终改进版
    """
    img1 = load_image(image_path1, grayscale=False)
    img2 = load_image(image_path2, grayscale=False)
    
    img1 = normalize_pixel_values(img1)
    img2 = normalize_pixel_values(img2)
    
    scores = []
    factor_names = [
        'Histogram Similarity',
        'Feature Comparison',
        'SSIM (Structural Similarity)',
        'NCC (Normalized Cross-Correlation)',
        'Rotated NCC'
    ]
    factor_scores = {}
    
    try:
        hist1 = calculate_histogram(img1, bins=32)
        hist2 = calculate_histogram(img2, bins=32)
        hist_sim = histogram_intersection(hist1, hist2)
        scores.append(hist_sim)
        factor_scores['Histogram Similarity'] = float(hist_sim)
    except:
        scores.append(0.5)
        factor_scores['Histogram Similarity'] = 0.5
    
    try:
        feat1 = extract_features(img1)
        feat2 = extract_features(img2)
        feat_sim = compare_features(feat1, feat2)
        scores.append(feat_sim)
        factor_scores['Feature Comparison'] = float(feat_sim)
    except:
        scores.append(0.5)
        factor_scores['Feature Comparison'] = 0.5
    
    best_angle = 0
    try:
        best_angle, rotated_ssim = find_best_rotation(img1, img2)
        original_ssim = calculate_ssim(img1, img2)
        best_ssim = max(original_ssim, rotated_ssim)
        scores.append(best_ssim)
        factor_scores['SSIM (Structural Similarity)'] = float(best_ssim)
    except:
        scores.append(0.5)
        factor_scores['SSIM (Structural Similarity)'] = 0.5
    
    try:
        ncc = calculate_ncc(img1, img2)
        scores.append(ncc)
        factor_scores['NCC (Normalized Cross-Correlation)'] = float(ncc)
    except:
        scores.append(0.5)
        factor_scores['NCC (Normalized Cross-Correlation)'] = 0.5
    
    try:
        if img2.ndim == 3:
            img2_gray = to_grayscale(img2)
        else:
            img2_gray = img2
        rotated = rotate_image_array(img2_gray, best_angle)
        if img1.ndim == 3:
            img1_gray = to_grayscale(img1)
        else:
            img1_gray = img1
        rotated_ncc = calculate_ncc(img1_gray, rotated)
        best_rotated_ncc = max(ncc, rotated_ncc)
        scores.append(best_rotated_ncc)
        factor_scores['Rotated NCC'] = float(best_rotated_ncc)
    except:
        scores.append(0.5)
        factor_scores['Rotated NCC'] = 0.5
    
    weights = [0.25, 0.20, 0.25, 0.15, 0.15]
    final_similarity = np.average(scores, weights=weights)
    final_similarity = max(0.0, min(1.0, final_similarity))
    
    result = {
        'similarity': float(final_similarity),
        'optimal_scale_level': 0,
        'factor_scores': factor_scores,
        'weights': {name: weight for name, weight in zip(factor_names, weights)}
    }
    
    if return_intermediate:
        result['intermediate'] = {
            'preprocessed1': img1,
            'preprocessed2': img2,
            'mask1': None,
            'mask2': None,
            'subject1': img1,
            'subject2': img2,
            'aligned1': img1,
            'aligned2': img2
        }
    
    return result


def get_similarity_label(similarity):
    if similarity >= 0.8:
        return "高度相似"
    elif similarity >= 0.6:
        return "相似"
    elif similarity >= 0.4:
        return "一般相似"
    elif similarity >= 0.3:
        return "不太相似"
    else:
        return "不相似"
