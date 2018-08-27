import matplotlib.pyplot as plt

xs = np.linspace(0, 10, 100) # 100 evenly spaced points in [0,10]
plt.plot(xs, np.sin(xs))
plt.plot(xs, np.cos(xs))
plt.show()
