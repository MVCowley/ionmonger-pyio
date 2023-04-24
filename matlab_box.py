import traceback
import matlab.engine

def run_im(device, path):
    eng = matlab.engine.start_matlab()
    eng.cd(path)
    try:
        matlab_device = matlab.double(device.tolist())
        sol = eng.master_func(matlab_device)
        output = eng.export_all(sol)
        # jv = eng.export_single_jv(sol)
        return output
    except Exception:
        print('Something went wrong')
        return traceback.format_exc()