import os
import datetime
import os.path
import subprocess as subp
import sys
import thread

file2 = open('selected1.txt')
line2 = file2.readlines()
file2.close()

selectedattr = line2[0].strip().split(',')

file1 = open('feature_filter.csv')
lines = file1.readlines()
file1.close()

result = open('feature_filter_selected.csv','w')

tmplist1=[]
for j in range(len(selectedattr)):
	tmplist1.append(str(j+1))
tmplist1.append(str(len(selectedattr)+1))
result.write(','.join(tmplist1)+'\n')

for i in range(1,len(lines)):
	allatt = lines[i].strip().split(',')
	tmplist = []
	for j in range(len(selectedattr)):
		tmplist.append(allatt[int(selectedattr[j])])
	tmplist.append('yes')
	result.write(','.join(tmplist)+'\n')

result.close()