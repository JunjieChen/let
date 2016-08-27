import math, random, os, time, shutil, string, sys

srcfile=open('nonduplicated_order_'+sys.argv[1])
srclines=srcfile.readlines()
srcfile.close()

result=open('finalresult_'+sys.argv[1],'w')
index=0
for i in range(len(srclines)):
	if int(srclines[i].strip().split(',')[0])==index:
		result.write(srclines[i].strip().split(',')[0]+','+srclines[i].strip().split(',')[1]+','+str(float(srclines[i].strip().split(',')[2])+float(sys.argv[2]))+'\n')

		index+=1
	elif int(srclines[i].strip().split(',')[0])>index:
		for j in range(index,int(srclines[i].strip().split(',')[0])+1):
			#result.write(srclines[i])
			result.write(srclines[i].strip().split(',')[0]+','+srclines[i].strip().split(',')[1]+','+str(float(srclines[i].strip().split(',')[2])+float(sys.argv[2]))+'\n')
		index=int(srclines[i].strip().split(',')[0])+1
result.close()
