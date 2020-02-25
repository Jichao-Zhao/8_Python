import numpy as np


# Box-Muller method convert Uniform distribution to Normal distribution.
# mu is expect. sigma is standard variance. size is number of sample.
def boxmullersampling(mu=0, sigma=1, size=1):
    u = np.random.uniform(size=size)
    v = np.random.uniform(size=size)
    z = np.sqrt(-2*np.log(u))*np.cos(2*np.pi*v)
    return mu+z*sigma

'''
# Test Box-Muller method.
list = boxmullersampling(mu=180,sigma=10,size=10000)
b = 0
for i in range(len(list)):
    if (list[i] > 150 and list[i] < 210):
        b = b + 1
print(b)
'''