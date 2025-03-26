import matplotlib.pyplot as plt
import numpy as np

x_axis = ['50,000', '5,000', '1,000', '500']
height = [20440.22948, 5.0856 , 3.668 , 3.108 ]
log_scale = 10*np.log(height)

# plot
fig, ax = plt.subplots()


ax.bar(x_axis, log_scale, width=1, edgecolor="white", linewidth=0.7)
ax.set(ylim=(min(log_scale)-1, max(log_scale)+3))

plt.title("Token average length vs dictionary size")
plt.xlabel('Dictionary Size')
plt.ylabel('Average token length (log scale)')
fig.savefig('token_length_comparison.jpg')

plt.show()