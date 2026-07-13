import numpy as np
from typing import Tuple
def compute_ndvi(nir_band: np.ndarray, red_band: np.ndarray) -> np.ndarray:
    nir, red = nir_band.astype(float), red_band.astype(float)
    denominator = nir + red
    denominator[denominator == 0] = 0.001
    return (nir - red) / denominator
def classify_vegetation(ndvi: np.ndarray) -> dict:
    return {'dense_vegetation': float(np.mean(ndvi > 0.6)), 'moderate': float(np.mean((ndvi > 0.3) & (ndvi <= 0.6))), 'sparse': float(np.mean((ndvi > 0.1) & (ndvi <= 0.3))), 'non_vegetation': float(np.mean(ndvi <= 0.1))}
def detect_change(before: np.ndarray, after: np.ndarray, threshold: float = 0.15) -> np.ndarray:
    diff = after - before
    change_map = np.zeros_like(diff)
    change_map[diff > threshold] = 1; change_map[diff < -threshold] = -1
    return change_map
