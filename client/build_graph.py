import matplotlib.pyplot as plt
import math
import os

time = range(0, 100)

files = []
for file in os.listdir("."):
    if file.endswith("0.data"):
        files.append(file)

files_avg = []

for file in os.listdir("."):
    if file.endswith("avg.data"):
        files_avg.append(file)

print(files_avg)

indexes = []

# delay
maxval = 0

fig, ax = plt.subplots(figsize=(16, 9))

for filename in files:
    i = int(int(filename.replace(".data", "")) / 10)
    indexes.append(i)
    if os.path.exists(filename):
        with open(filename, "r") as data_file:
            per_accounts_median = []
            per_accounts_std = []
            for line in data_file.readlines():
                parts = line.split('\t')
                delay_val = int(parts[0])
                if maxval < delay_val:
                    maxval = delay_val
                per_accounts_median.append(delay_val)
            plt.plot(time, per_accounts_median, marker='o', label=f"{i * 10}")
ax.set_ylim([0, maxval * 1.1])
ax.legend(title='# of sensor nodes', loc='upper right')
plt.xlabel('execution time (# of readings submitted)')  # rep of uploading values to blockchain
plt.ylabel('median delay to commit (ms)')
plt.title('Median ATTACK')
plt.savefig("delay.png")


# for filename in files_avg:
#     i = int(int(filename.replace("avg.data", "")) / 10)
#     indexes.append(i)
#     if os.path.exists(filename):
#         with open(filename, "r") as data_file:
#             per_accounts_median = []
#             per_accounts_std = []
#             for line in data_file.readlines():
#                 parts = line.split('\t')
#                 delay_val = float(parts[0])
#                 if maxval < delay_val:
#                     maxval = delay_val
#                 per_accounts_median.append(delay_val)
#             plt.plot(time, per_accounts_median, marker='o', label=f"{i * 10}")
# ax.set_ylim([0, maxval * 1.1])
# ax.legend(title='# of sensor nodes', loc='upper right')
# plt.xlabel('execution time (# of readings submitted)')  # rep of uploading values to blockchain
# plt.ylabel('average delay to commit (ms)')
# plt.title('Average delay to commit a reading over time of execution')
# plt.savefig("delay_avg.png")


# variance

fig, ax = plt.subplots(figsize=(16, 9))

for filename in files:
    i = int(int(filename.replace(".data", "")) / 10)
    indexes.append(i)
    if os.path.exists(filename):
        with open(filename, "r") as data_file:
            per_accounts_std = []
            for line in data_file.readlines():
                parts = line.split('\t')
                per_accounts_std.append(float(parts[1]))
            plt.plot(time, per_accounts_std, marker='o', label=f"{i * 10}")
ax.set_ylim([0, (maxval * maxval) * 0.15])
ax.legend(title='# of sensor nodes', loc='upper right')
# plt.xlabel('execution time (# of readings submitted)')  # rep of uploading values to blockchain
# plt.ylabel('delay variance to commit (ms^2)')
plt.title('Variance attack!!!!!!')
plt.savefig("variance.png")

# standard deviation

fig, ax = plt.subplots(figsize=(16, 9))

for filename in files:
    i = int(int(filename.replace(".data", "")) / 10)
    indexes.append(i)
    if os.path.exists(filename):
        with open(filename, "r") as data_file:
            per_accounts_std = []
            for line in data_file.readlines():
                parts = line.split('\t')
                per_accounts_std.append(float(parts[2]))
            plt.plot(time, per_accounts_std, marker='o', label=f"{i * 10}")
ax.set_ylim([0, maxval * 1.1])
ax.legend(title='# of sensor nodes', loc='upper right')
# plt.xlabel('execution time (# of readings submitted)')  # rep of uploading values to blockchain
# plt.ylabel('delay std to commit (ms)')
plt.title('STD attack!!!!!!!')
plt.savefig("std.png")
