from matplotlib import pyplot as plt

with open("data.txt", "r") as f:
    raw_data = f.read().split("\n")

data = []
last_item = None
for item in raw_data:
    try:
        if item != last_item:
            data.append(int(item))
            last_item = item
    except ValueError:
        continue

y = list(range(len(data)))

plt.scatter(data, y)
plt.plot(data, y)
plt.show()

# from vispy.plot import Fig
#
# fig = Fig()
# ax_left = fig[0, 0]
# ax_right = fig[0, 1]
# ax_left.plot(data)
# ax_right.histogram(y)