import numpy as np
import matplotlib.pyplot as plt

a = [1,22,13,54,6,12,6,7]
b = [122,341,4,5,72,6,7,2,42,10]


np_a = np.array(sorted(a))
np_b = np.array(sorted(b))

result = np.ones(np_a.shape,dtype='int32')
for x in np_b:
    tmp = np.array([x]) + np_a
    result = np.vstack((result, tmp))
result[1:]

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')

ax.table(cellText=result[1:], colLabels=np_a, rowLabels=np_b, loc='upper center')
plt.show()