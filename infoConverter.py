# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 23:27:30 2014

@author: Kang Liu (kang.liu@tum.de)

This script convert `infos.dat` generated from OpenCv to `I00***.txt` format,
which is accepted by Piotr's Image & Video Matlab Toolbox 

USAGE


"""

from os import path
import os

def generate(input_dir):
	# input
	
	info_fname = path.join(input_dir, "infos.dat")
	# output
	output_dir = path.join(input_dir, "posGt", "")
	if not path.isdir(output_dir):
			os.makedirs(output_dir)

	fileIn = open(info_fname, 'r')

	for eachLine in fileIn:
		inList = eachLine.split()
		outList=['person', '0', '0', inList[4], inList[5],\
		'0', '0', '0', '0', '0', '0', '0']
		outLine=' '.join(outList)    
		outStr='% bbGt version=3\n' + outLine + '\n'
		fname=inList[0].split("/")[1].replace('.tif','') + ".txt"
		fileOut = open(path.join(output_dir, fname),'w')
		fileOut.write(outStr)
		fileOut.close()

	fileIn.close()
	#print outStr

if __name__ == '__main__':
	angle_list = [x/10.0 for x in range(0, 1800, 225)] # a trick to generate angle list every 22.5 degree
	for i in angle_list:
		sample_dir = '/home/kang/datasets/DetectTrain/train/Vaihingen'
		sample_dirname = 'offset' + str(i)
		sample_fulldir = path.join(sample_dir, sample_dirname)
		print sample_fulldir
		generate(sample_fulldir)






