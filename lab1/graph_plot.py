from matplotlib import pyplot as plt

""" 
input      b       i       s
5000     1.690   0.857   1.556
10000    6.654   3.557   6.033
15000    14.732  7.978   13.955
20000    27.002  14.393  25.538  
 """
x_axis = [5000, 10000, 15000, 20000]
y_axis = [1.556, 6.033, 13.955, 25.538]


plt.plot(x_axis, y_axis, marker="o", color="green")
plt.xlabel("Selection Sort")
plt.ylabel("Time (Sec)")
plt.title("Input Size")
plt.show()
