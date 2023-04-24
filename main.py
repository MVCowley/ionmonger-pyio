if __name__ == '__main__':
    import json
    import traceback
    import pandas as pd
    import multiprocessing as mp
    from matlab_box import run_im
    from param_gen import param_array

    
    PATH = r'/home/mvc28/ionmonger-simulations/IonMonger'
    PROCESSES = 16
    # FACTORS = 32
    # RESOLUTION = 9
    # LEVELS = pd.read_csv('levels.csv')

    devices_pd = pd.read_csv('analysis_devices.csv')
    devices = devices_pd.to_numpy()[:, 1:]

    with mp.Pool(processes=PROCESSES) as pool:
        async_results = [pool.apply_async(run_im, (device, PATH)) for device in devices]
        for index, res in enumerate(async_results):
            try:
                result = res.get(timeout=120)
                py_result = {}
                if type(result) is str:
                     py_result = result
                     print(f'MATLAB error for device {index}, check output for traceback')
                else:
                    for key in result.keys():
                            py_result[key] = [i for i in result[key]._data]
                    print(f'Device {index} solved by IM')
            except TimeoutError:
                py_result = "timeout"
                print(f'Device {index} timed out')
            except Exception:
                 py_result = traceback.format_exc()
                 print(f'Device {index} threw an error, check output for traceback')

            with open(f'/home/mvc28/ionmonger-simulations/data/steady_state/device_subset_light_static/device_{index}.txt', 'w') as result_file:
                    result_file.write(json.dumps(py_result))