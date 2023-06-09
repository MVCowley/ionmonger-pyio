if __name__ == '__main__':
    import json
    import traceback
    import pandas as pd
    import multiprocessing as mp
    from matlab_box import run_im
    from param_gen import param_array

    
    PATH = # Place path to IonMonger here
    PROCESSES = 16 # Number of parallel processes
    
    # Can either generate a set of devices using param_array, or provide own dataframe to devices
    FACTORS = 32
    RESOLUTION = 9
    LEVELS = pd.read_csv('levels.csv')
    devices = param_array(FACTORS, RESOLUTION, LEVELS)

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

            with open(f'/path_to_directory/{index}.txt', 'w') as result_file:
                    result_file.write(json.dumps(py_result))
