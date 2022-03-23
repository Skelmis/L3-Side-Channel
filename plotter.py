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

def get_array_sizes(size) -> list[float]:
    """Returns .5mb chunks"""
    data = []
    for i in range(0, size):
        data.extend([i, i+0.5])
    data.append(size)
    return data


# plt.xlabel("Array index")
# plt.ylabel("Index lookup time in nanoseconds")
# plt.xticks(get_array_sizes(len(data)))
# plt.show()
# plt.savefig('plots/initial_laptop_1.png')


fig, ax = plt.subplots()

ax.set_title("Size vs access time")
ax.set_ylabel("Index lookup time in nanoseconds")
ax.set_xlabel("Array @ mb size")

# Underlying values
mb = 4
n = mb * 2 + 1
step = (len(data) - 0) // (n - 1)
x = list(range(0, len(data), step))
# x.insert(0, 0)
ticks = get_array_sizes(mb)

ax.set_xticks(x)
ax.set_xticklabels(ticks)

ax.plot(y, data)
# plt.plot(y, data)
plt.show()
# plt.savefig('plots/initial_laptop_2.png')