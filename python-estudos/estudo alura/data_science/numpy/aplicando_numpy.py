import numpy as np

x = [0,1,2,3,4,5,6,7,8,9,10]
y = []

for i in x:
    y.append(i + 3 / 2)   

print(y)


b = [0,1,2,3,4,5,6,7,8,9,10]
b = np.array(b)
c = b + 3 / 2
print(c)