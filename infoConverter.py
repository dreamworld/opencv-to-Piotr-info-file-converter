# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 23:27:30 2014

@author: Kang Liu (kang.liu@tum.de)

This script convert `infos.dat` generated from OpenCv to `I00***.txt` format,
which is accepted by Piotr's Image & Video Matlab Toolbox 

USAGE


"""

fileIn = open('tmp/infos.dat', 'r')

outStr = ''
for eachLine in fileIn:
    inList = eachLine.split()
    outList=['person', '0', '0', inList[4], inList[5],\
    '0', '0', '0', '0', '0', '0', '0']
    outLine=' '.join(outList)    
    outStr+=outLine+'\n'

fileIn.close()
print outStr
fileOut = open('tmp/abc.txt','w')
fileOut.write(outStr)
fileOut.close()