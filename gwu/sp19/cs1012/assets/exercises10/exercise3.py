import matplotlib.pyplot as plt
import numpy as np

# experimental or sampled values, two columns : time and y value    
data = np.loadtxt("signaldata.txt")

# expected or desired values
mu = data[:,1].mean()
sigma = np.std(data[:,1])

x = np.arange(len(data[:,1]))

# compute error for each sample
err = np.abs( data[:,1] - np.sin(data[:,0]) )

# plot the error
plt.plot(x, err, label='error', marker='o', linestyle='None')
# plot the mean line
plt.plot((0,x[-1]), (mu,mu), label='mean')
# plot the stddev line
plt.plot((0,x[-1]), (sigma,sigma), label='stddev')
# labeling
plt.xlabel('Sample')
plt.ylabel('Error')
plt.title('Signal Error')
plt.legend()

plt.savefig("exercise3.png", dpi=120)