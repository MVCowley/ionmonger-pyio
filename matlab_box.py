import traceback
import matlab.engine

def run_im(device, path):
    eng = matlab.engine.start_matlab()
    eng.cd(path)
    try:
        matlab_device = matlab.double(device.tolist())
        sol = eng.master_func(matlab_device)
        jv = eng.export_single_jv(sol)
        return jv
    except Exception:
        print('Something went wrong')
        return traceback.format_exc()