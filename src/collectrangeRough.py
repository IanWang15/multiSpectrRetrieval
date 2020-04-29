import numpy as np
import os
import re

class main():
        def checkrange(self, line):
            #return ((line[2] < -35.81251) and (line[2] > -56.94899) and (line[3] < 0))#-37.95007) and (line[3] > -66.85692))
            return ((line[0] < -42.82366) and (line[0] > -60.56628) and (line[1] < 159.3183) and (line[1] > 124.5528))

        def checkfile(self, rfile):
            return (self.checkrange(rfile[0,:]) or self.checkrange(rfile[-1,:]))

t = main()

add1='/scratch/user/yiwang_atmo/run/03262020/2013run/245/out_RougValue/'
fmc6=open('../data/f_misr20132450010RougValuemc6.txt','w')
f2hm=open('../data/f_misr20132450010RougValue2hm.txt','w')

names1 = os.listdir(add1)

for ifile in range(0,len(names1)): # loop of file
    str_arr = re.findall(r"\d*",names1[ifile])
    a = np.loadtxt(add1+names1[ifile],dtype=float)
    print(names1[ifile])

    if (a.ndim != 1):  # check null file
        if (len(a) >= 1):
            if t.checkfile(a):
                print('within the area: ', names1[ifile])
                for iline in range(0,len(a)):
                    if t.checkrange(a[iline,:]):
                        if a[iline,2] == 0:
                            fmc6.write(str(a[iline,0])+' '+str(a[iline,1])+' '+str(a[iline,2])+\
                            ' '+str(a[iline,3])+' '+str(a[iline,4])+' '+str(a[iline,5])+\
                            ' '+str(a[iline,6])+' '+str(a[iline,7])+' '+str(a[iline,8])+\
                            ' '+str(a[iline,9])+' '+str(a[iline,10])+' '+str(a[iline,11])+\
                            ' '+str(a[iline,12])+'\n')
                        else:
                            f2hm.write(str(a[iline,0])+' '+str(a[iline,1])+' '+str(a[iline,2])+\
                            ' '+str(a[iline,3])+' '+str(a[iline,4])+' '+str(a[iline,5])+\
                            ' '+str(a[iline,6])+' '+str(a[iline,7])+' '+str(a[iline,8])+\
                            ' '+str(a[iline,9])+' '+str(a[iline,10])+' '+str(a[iline,11])+\
                            ' '+str(a[iline,12])+'\n')

# lat,lon,ArrValue[iRougValue[0]], cnt, COT_sa[k],CPress_sa[k],CRe[k],CTT[k],sza[k,8],Hsigma[k],CTHMOD[k],CTHMISR[k],RougValue[k,iRougValue[0]]
#         0: mc6; 0.0001: 2hm

print('computation is finished')
