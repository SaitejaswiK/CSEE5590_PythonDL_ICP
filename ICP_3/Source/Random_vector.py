import numpy as np

x = np.random.rand(15)
print("Input:\n")
print(x)

x[x.argmax()] = 100
print(x)