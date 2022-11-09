import numpy as np

f1 = np.array([[0, 2], [2, 3]]) * 1
f2 = np.array([[6, 5], [4, 7]]) * -1
f3 = f1 + f2

max_result = np.max(f3)

print(max_result)


blank = np.zeros((400, 400), dtype="uint8")
print(len(blank[0][0]))
