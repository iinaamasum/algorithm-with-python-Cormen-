import matplotlib.pyplot as plt

x_axis = [5000, 10000, 15000, 20000, 25000]
y_axis_worst = [0.124, 0.208, 0.391, 0.718, 0.834]
y_axis_best = [00.004, 0.005, 0.006, 0.008, 0.007]
y_axis_avg = [0.071, 0.107, 0.189, 0.453, 0.573]

Y = {"red": y_axis_worst, "green": y_axis_avg, "blue": y_axis_best}

for key, val in Y.items():
    plt.plot(x_axis, val, marker="o", color=key)

plt.xlabel("Input Size")
plt.ylabel("Time (mille-seconds")
plt.title("Linear Search: Worst(Red) Average(Green) Best(Blue)")
plt.show()
