from matplotlib import pyplot as plt

with open("loop_lookups.txt", "r") as f:
    raw_data = f.read().split("\n")

data = []
last_item = None
for item in raw_data:
    try:
        if item != last_item or 1 == 1:
            data.append(int(item))
            last_item = item
    except ValueError:
        continue


def get_array_sizes(size) -> list[float]:
    """Returns .5mb chunks"""
    data = []
    for i in range(0, size):
        data.extend([i, i + 0.5])
    data.append(size)
    return data


fig, ax = plt.subplots()

ax.set_title("Size vs access time")
ax.set_ylabel("Index lookup time in nanoseconds")
ax.set_xlabel("Array size in MB")

# Underlying values
mb = 8
n = mb * 2 + 1
step = (len(data) - 0) // (n - 1)
x = list(range(0, len(data), step))
x.append(15)
ticks = get_array_sizes(mb)

# Set y axis right based off max size
tick_step = (max(data) - 0) // (n - 1)
y_ticks = []
for i in range(0, max(data), tick_step):
    y_ticks.append(i)


ax.set_xticks(x)
ax.set_xticklabels(ticks)

# Same data as labels so no biggie
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

ax.plot(list(range(len(data))), data)
# plt.plot(y, data)
# plt.show()
plt.savefig("final_loop.png")
