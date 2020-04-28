# reading the remote sensing retrievals from Visible and thermal IR.

import numpy as np

class main():
        def readfile(self, filename):
                filedata = np.loadtxt(filename, comments='#')
                return filedata

t = main()

vismc6path = '/scratch/user/yiwang_atmo/Chia_Pang/Cloud_Retrieval/SatalliteData/MODIS_Hioki/A2013245.1320_obs.inv.rad.rev4'
vismc6 = t.readfile(vismc6path)

irmc6path = '/scratch/user/yiwang_atmo/Chia_Pang/Cloud_Retrieval/OptimalEstimate/Retrieval_DISORT/result/Output_Ret_MOD_CldM_02.txt'
irmc6 = t.readfile(irmc6path)

print('ok?')
#irthmpath = '../data/A2006253.1350-1605_obs.inv.rad.rev4'
#irthm = t.readfile(irthmpath)

f=open('../data/f_VIS_IR03262020.txt','w')

last1 = 0
last2 = 0
for i in range(len(irmc6)):
    if irmc6[i,5] < 21: # and irData[i, 3] < 0.0001:
        f.write(str(vismc6[i,12])+' '+str(vismc6[i,18])+' '+str(irmc6[i,0])+\
' '+str(vismc6[i,1])+' '+str(vismc6[i,2])+' '+str(vismc6[i,6])+\
' '+str(vismc6[i,9])+' '+str(vismc6[i,10])+' '+str(vismc6[i,11])+\
'\n')
            #                        VIS tau                    IR tau               

print('computation is finished')
