import matlab.engine

def run_im(device, path):
    eng = matlab.engine.start_matlab()
    eng.cd(path)
    try:
        sol = eng.master_func(device)
        jv = eng.export_single_jv(sol)
        return jv
    except:
        print('Something went wrong')
        return 'Exception error'