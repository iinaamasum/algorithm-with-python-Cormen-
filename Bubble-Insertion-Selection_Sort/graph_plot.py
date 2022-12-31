from matplotlib import pyplot as plt

""" 
input      b       i       s
5000     1.690   0.857   1.556
10000    6.654   3.557   6.033
15000    14.732  7.978   13.955
20000    27.002  14.393  25.538  
 """
x_axis = [5000, 10000, 15000, 20000]
y_axis_b = [1.556, 6.033, 13.955, 25.538]
y_axis_i = [0.857, 3.557, 7.978, 14.978]
y_axis_s = [1.690, 6.654, 14.732, 27.002]

y_variable = {"red": y_axis_b, "green": y_axis_i, "blue": y_axis_s}
# colors = ["red", "blue", "green"]

# for key, val in y_variable.items():
#     # print(key)
#     plt.plot(x_axis, val, marker="o", color=key)

plt.plot(x_axis, y_axis_s, marker="o", color="blue")

plt.xlabel("Input Size")
plt.ylabel("Time (Sec)")
plt.title("Selection Sort")
plt.show()
