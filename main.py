if __name__ == '__main__':
    import pandas as pd
    import multiprocessing as mp
    from matlab_box import run_im
    from param_gen import param_array

    FACTORS = 32
    RESOLUTION = 9
    LEVELS = pd.read_csv('levels.csv')

    devices = param_array(FACTORS, RESOLUTION, LEVELS)
    pool = mp.Pool()
    results = [pool.apply(run_im, args=([device])) for device in devices]
    pool.close()
    print(results)


# from matlab_box import run_im
# from param_gen import param_array

# FACTORS = 32
# RESOLUTION = 9
# LEVELS = 'levels.csv'

# devices = param_array(FACTORS, RESOLUTION, LEVELS)

# def device_loop(devices):
#     for i in range(len(devices)):
#         device = devices[i]
#         jv = run_im(device)
#         print(jv)

# device_loop(devices)