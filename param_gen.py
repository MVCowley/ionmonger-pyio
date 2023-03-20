import numpy as np
import pyDOE2.doe_factorial as pyfac

def param_array(factors, resolution, level_index):

    fac_matrix = pyfac.fracfact_by_res(factors, resolution)

    np.putmask(fac_matrix, fac_matrix == -1, level_index.iloc[0])
    np.putmask(fac_matrix, fac_matrix == 1, level_index.iloc[1])

    return fac_matrix
