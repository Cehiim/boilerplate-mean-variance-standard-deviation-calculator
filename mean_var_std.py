import numpy as np

def calculate(list):
    try:
        array = np.array(list, dtype=np.float64).reshape(3, 3)

        mean_columns = array.mean(axis=0).tolist()
        mean_rows = array.mean(axis=1).tolist()
        mean = float(array.mean())

        var_columns = array.var(axis=0).tolist()
        var_rows = array.var(axis=1).tolist()
        var = float(array.var())

        std_columns = array.std(axis=0).tolist()
        std_rows = array.std(axis=1).tolist()
        std = float(array.std())

        max_columns = array.max(axis=0).tolist()
        max_rows = array.max(axis=1).tolist()
        max = float(array.max())

        min_columns = array.min(axis=0).tolist()
        min_rows = array.min(axis=1).tolist()
        min = float(array.min())

        sum_columns = array.sum(axis=0).tolist()
        sum_rows = array.sum(axis=1).tolist()
        sum = float(array.sum())

        calculations = {
            "mean": [mean_columns, mean_rows, mean], 
            "variance": [var_columns, var_rows, var],
            "standard deviation": [std_columns, std_rows, std],
            "max": [max_columns, max_rows, max],
            "min": [min_columns, min_rows, min],
            "sum": [sum_columns, sum_rows, sum]
        }

        return calculations

    except ValueError:
        raise ValueError("List must contain nine numbers.")