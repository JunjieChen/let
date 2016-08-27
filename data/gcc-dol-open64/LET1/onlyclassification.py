import math, random, os, time, shutil, string, sys

start = time.time()
pp=open('prob_per.csv')
llines=pp.readlines()
pp.close()

save=dict()

for i in range(len(llines)):
	save[llines[i].strip().split(' = ')[0]]=float(llines[i].strip().split(' = ')[-1])

savelist=sorted(save.iteritems(), key=lambda d:d[1], reverse = True)

resultdic=open("prob_order.csv",'w')


# prob2000=open('../p_order.csv')
# prob2000lines=prob2000.readlines()
# prob2000.close()

# for i in range(1000):
# 	resultdic.write(prob2000lines[i])

for k in range(len(savelist)):
	resultdic.write(savelist[k][0] + ' = ' + str(savelist[k][1]) + '\n')

resultdic.close()
order = open("prob_order.csv")
for line in order.xreadlines():
	nPos = line.index(' = ')
	filename = line[:nPos]
	# print filename

	# selectedpath = '/SEIDISK/chenjj/compiler/clusterspeedup/test/onlyclassification/programs/' + filename 

	# os.system("cp " + selectedpath + " /SEIDISK/chenjj/compiler/clusterspeedup/test/onlyclassification/csmith-2.2.0/runtime")
			
	# os.system("./run_cluster.sh " + filename[:-2])
	end = time.time()
	elapsed = end - start

	fselectedfilenameorder = file(sys.argv[1],'a+')
	fselectedfilenameorder.write(filename + "\n")

	ftime = file('selectiontime_' + sys.argv[1],'a+')
	ftime.write(str(elapsed) + "\n")

fselectedfilenameorder .close()
ftime.close()

os.system("python dicttime.py " + sys.argv[1] + " " + sys.argv[2])
os.system("python distinguishcluster.py " + sys.argv[1] + " " + sys.argv[2])

order.close()