import matplotlib.pyplot as plt

x_axis = [5000, 10000, 15000, 20000, 25000]
y_axis_best = [0.001, 0.003, 0.002, 0.001, 0.005]
y_axis_worst = [0.044, 0.051, 0.062, 0.086, 0.072]
y_axis_avg = [0.021, 0.038, 0.046, 0.053, 0.057]

Y = {"red": y_axis_worst, "green": y_axis_avg, "blue": y_axis_best}

for key, val in Y.items():
    plt.plot(x_axis, val, marker="o", color=key)

plt.xlabel("Input Size")
plt.ylabel("Time (mille-seconds)")
plt.title("Binary Search: Worst(Red) Average(Green) Best(Blue)")
plt.show()
