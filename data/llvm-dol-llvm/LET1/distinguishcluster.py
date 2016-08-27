import math, random, os, time, shutil, dircache, sys, string

f = file('nonduplicated_' + sys.argv[1],'a+')
f1 = file('nonduplicated_order_' + sys.argv[1],'a+')

namelist = []
order = 0
count = 0
faultprogram = open(sys.argv[1])

ordertime1 = open(sys.argv[2])
timelist1=[]
for linetime1 in ordertime1.xreadlines():
	timelist1.append(string.atof(linetime1[:-1]))


ordertime2 = open('selectiontime_' + sys.argv[1])
timelist2=[]
for linetime2 in ordertime2.xreadlines():
	timelist2.append(string.atof(linetime2[:-1]))

timelist=[]
for i in range(0, len(timelist1)):
	timelist.append(timelist1[i] + timelist2[i])

for line in faultprogram.xreadlines():
	count += 1
	if 'variant' in line:

		pragramname=line[:-1]

		#print(pragramname)

		faultcluster = open("llvm_all.csv")
		for line1 in faultcluster.xreadlines():
			nPos = line1.index(',')
			clustername=line1.strip().split(',')[-1]
			if pragramname in line1:
				if clustername not in namelist:
					#print clustername
					namelist.append(clustername)
					f.write(clustername)
					order += 1
					
					

					f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
					
				else:
					f.write('duplicated' + '\n')	
					f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
				break
		faultcluster.close()
	else:
		f.write('correct' + '\n')
		f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
f.close()
f1.close()
faultprogram.close()
ordertime1.close()
ordertime2.close()
