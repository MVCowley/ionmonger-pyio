import matlab.engine

def run_im(device):
    PATH = r'C:\Users\mvc28\OneDrive - University of Bath\work\IonMonger'
    eng = matlab.engine.start_matlab()
    eng.cd(PATH)
    try:
        print(device)
        sol = eng.master_func(device)
        jv = eng.export_single_jv(sol)
        # clear eng enviroment before quitting
        return jv
    except:
        print('oops')