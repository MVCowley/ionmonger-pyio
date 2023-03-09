import numpy as np
import pandas as pd
from param_gen import param_array

FACTORS = 32
RESOLUTION = 9
LEVELS = pd.read_csv('levels.csv')

def test_pa_shape():
    devices = param_array(FACTORS, RESOLUTION, LEVELS)
    assert devices.shape == (FACTORS**2, FACTORS)

def test_pa_shape():
    devices = param_array(FACTORS, RESOLUTION, LEVELS)
    assert np.isnan(devices).any() == False

def test_pa_mean():
    low_level = np.full(32, -1)
    high_level = np.full(32, 1)
    levels = pd.DataFrame.from_records(np.stack([low_level, high_level]))
    print(levels)
    devices = param_array(FACTORS, RESOLUTION, levels)
    devices_mean = np.mean(devices, axis=0)
    assert (devices_mean == np.zeros_like(devices_mean)).all()