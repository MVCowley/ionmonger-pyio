import numpy as np
import pandas as pd
import pyDOE2.doe_factorial as pyfac

def param_array(factors, resolution, level_index):

    fac_matrix = pyfac.fracfact_by_res(factors, resolution)

    np.putmask(fac_matrix, fac_matrix == -1, level_index.iloc[0])
    np.putmask(fac_matrix, fac_matrix == 1, level_index.iloc[1])

    return fac_matrix

# fac_matrix = pyfac.fracfact_by_res(32, 3)[:4]
# # fac_matrix_mean = np.mean(fac_matrix, axis=0)
# print(fac_matrix.shape)

# import matplotlib.pyplot as plt

# plt.bar(np.linspace(1, 31, 32), fac_matrix_mean)
# plt.show()