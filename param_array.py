import pandas as pd

class ParamArray():
  
    def __init__(self, data):
        self.data = data

    @classmethod
    def read_csv(cls, filename):
        data = pd.read_csv(filename)
        return cls(data)