if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import multiprocessing as mp
    from matlab_box import run_im
    from param_gen import param_array

    
    PATH = r'C:\Users\mvc28\OneDrive - University of Bath\work\IonMonger'
    FACTORS = 32
    RESOLUTION = 9
    LEVELS = pd.read_csv('levels.csv')

    devices = param_array(FACTORS, RESOLUTION, LEVELS)[:4] # cap on processes

    with mp.Pool(processes=4) as pool:
        async_results = [pool.apply_async(run_im, (device, PATH)) for device in devices]
        results = [None] * len(async_results)
        for index, res in enumerate(async_results):
            try:
                results[index] = res.get(timeout=120)
            except:
                results[index] = "timeout"

    results = np.asarray(results, dtype=object)
    np.savetxt('results.csv', results, delimiter=',')