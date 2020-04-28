# plotting comparison of retrievals between IR and VIS.
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility

filedata = np.loadtxt('../data/f_VIS_IR03262020_im03.txt', comments='#')

fig = plt.figure(figsize=(6.1,5))
ax=fig.add_subplot(111)
#plt.scatter(filedata[:,1], filedata[:,2], c='navy', alpha=0.05, edgecolor='none')
hb = ax.hexbin(filedata[:,1], filedata[:,2], gridsize=(45,50), cmap=plt.cm.Greens)

plt.axis([0, 5, 0, 5])
cb = fig.colorbar(hb)
cb.set_ticks(np.linspace(hb.get_array().min(), hb.get_array().max(), 6))
cb.set_ticklabels(np.linspace(0, 1., 6))
cb.set_label('Normalized Count', fontsize=16)
cb.ax.tick_params(labelsize=16)

ax.set_xlabel(r'$\tau$'+' (shortwave bands)', fontsize=16)
ax.set_ylabel(r'$\tau$'+' (thermal IR bands)', fontsize=16)
#ax42.set_ylabel('Normalized Frequency', fontsize=10)
ax.set_title('Two Hibit model (THM)', fontsize=16)
ax.set_xlim(0,5)
ax.set_ylim(0,5)
#ax.set_xticklabels(fontsize=14)
ax.tick_params(labelsize=16)

x = np.arange(6)
y = np.arange(6)

plt.plot(x, y, c='black', linewidth=0.5)
ax.text(0.2, 4.5, '(b)', fontsize = 18)

pngname = "../fig/"+"figScattHex_im03"+".pdf"
print("save ", pngname)
plt.savefig(pngname, dpi=100, facecolor='w', edgecolor='w',
    orientation='portrait', papertype=None, format=None,
    transparent=False, bbox_inches='tight', pad_inches=0.1)

plt.show()
