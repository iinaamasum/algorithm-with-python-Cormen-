import matplotlib.pyplot as plt

x_axis = [5000, 10000, 15000, 20000, 25000]
y_axis_worst = [0.089, 0.106, 0.115, 0.116, 0.119]
y_axis_best = [0.001, 0.003, 0.003, 0.004, 0.006]
y_axis_avg = [0.066, 0.072, 0.077, 0.079, 0.0893]

Y = {"red": y_axis_worst, "green": y_axis_avg, "blue": y_axis_best}

for key, val in Y.items():
    plt.plot(x_axis, val, marker="o", color=key)

plt.xlabel("Input Size")
plt.ylabel("Time (mille-seconds")
plt.title("Linear Search: Worst(Red) Average(Green) Best(Blue)")
plt.show()
