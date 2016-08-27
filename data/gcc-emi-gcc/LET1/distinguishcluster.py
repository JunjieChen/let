import math, random, os, time, shutil, dircache, sys, string

flistvariant = open('listvariant.csv')
distvariant = {}
for dv in flistvariant.xreadlines():
	vlist = dv[:-1].split(',')
	distvariant[vlist[0]] = vlist

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
		pragramname_list=[]

		#print(pragramname)
		pragramname_list.append(pragramname)
		for jk in range(1, len(distvariant[pragramname])):
			pragramname_list.append(distvariant[pragramname][jk])
		
		
		yes = 0
		for ii in range(0, len(pragramname_list)):
			faultcluster = open("emi_all.csv")
			for line1 in faultcluster.xreadlines():
				nPos = line1.index(',')
				clustername=line1.strip().split(',')[-1]

			

				if pragramname_list[ii] in line1:
					if clustername not in namelist:
						#print pragramname_list[ii]
						namelist.append(clustername)
						#f.write(clustername)
						order += 1
						yes = 1
					

						#f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
					
					#else:
						#f.write('duplicated' + '\n')	
						#f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
					break
			faultcluster.close()
		if yes == 1:
			f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
		else:
			f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
	else:
		#f.write('correct' + '\n')
		f1.write(str(order) + ',' + str(count) + ',' + str(timelist[count - 1]) + '\n')
f.close()
f1.close()
faultprogram.close()
ordertime1.close()
ordertime2.close()
flistvariant.close()