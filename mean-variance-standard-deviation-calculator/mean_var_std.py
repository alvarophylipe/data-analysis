import numpy as np

def calculate(arr):
  if len(arr) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr1 = np.array(arr).reshape(3,3)
    mean = [list(np.mean(arr1, axis= 0)), list(np.mean(arr1, axis = 1)), np.mean(arr1)]
    variance = [list(np.var(arr1, axis= 0)), list(np.var(arr1, axis = 1)), np.var(arr1)]
    stddev = [list(np.std(arr1, axis= 0)), list(np.std(arr1, axis = 1)), np.std(arr1)]
    max = [list(np.max(arr1, axis= 0)), list(np.max(arr1, axis = 1)), np.max(arr1)]
    min = [list(np.min(arr1, axis= 0)), list(np.min(arr1, axis = 1)), np.min(arr1)]
    sum = [list(np.sum(arr1, axis= 0)), list(np.sum(arr1, axis = 1)), np.sum(arr1)]

    calculations = {
      'mean': mean,
      'variance': variance,
      'standard deviation': stddev,
      'max': max,
      'min': min,
      'sum': sum
    }

    return calculations