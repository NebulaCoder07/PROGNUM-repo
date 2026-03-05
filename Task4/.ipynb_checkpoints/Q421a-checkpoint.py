import numpy as np
from scipy import stats
set1 = np.random.normal(0,1,10000)
set2 = np.random.normal(2,1,10000)

set1 = np.array(set1,dtype=np.dtype(np.float16))    # for memory resons
set2 = np.array(set2,dtype=np.dtype(np.float16))    # for memory resons

pdf1 = stats.norm.pdf(np.sort(set1), 0, 1)
pdf2 = stats.norm.pdf(np.sort(set2), 2, 1)

label1 = "X"
label2 = "Y"
label1_pdf = "X(PDF)"
label2_pdf = "Y(PDF)"


plt.figure(figsize=(10,8))
plt.hist(set1, density = True, bins = 30, label=label1, color='royalblue', ec = 'k',alpha = 0.5)
plt.hist(set2, density = True, bins = 30, label=label2, color='red',ec = 'k', alpha = 0.5)
plt.plot(np.sort(set1),pdf1, color='black', linewidth = 4,label=label1_pdf, linestyle = ":")
plt.plot(np.sort(set2),pdf2, color='black', linewidth = 4,label=label2_pdf, linestyle = "--")

#plt.rc("text", usetex = True)
plt.xlim(-6,8)
plt.xticks(range(-6,9), fontsize = 15)
plt.yticks(fontsize = 15)

plt.title('1D Histogram + PDF', fontsize = 20)
plt.xlabel("Values", fontsize = 15)
plt.ylabel("Probability Density", fontsize = 15)

plt.arrow(5, 0.15, -.5, 0, width=0.01, head_length = 0.5, head_width = 0.025, color="red")
plt.annotate(r'$\mathcal{N}(2,1)$',xy=(5.1, 0.143), color = 'red',fontsize = 20)

plt.arrow(-3, 0.15, .5, 0, width=0.01, head_length = 0.5, head_width = 0.025, color="blue")
plt.annotate(r'$\mathcal{N}(0,1)$',xy=(-4.6, 0.143), color = 'blue',fontsize = 20)

plt.grid(axis = 'y',color = 'lightgrey', linestyle = '--')
plt.legend(fontsize = 15)

plt.show()