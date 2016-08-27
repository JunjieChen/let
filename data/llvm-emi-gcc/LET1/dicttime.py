import math, random, os, time, shutil, string, sys

time = open('time_all.txt')
dictt={}
for line in time.xreadlines():
	nPos = line.index(',')
	programname = line[:nPos]
	
	timecnt = line[nPos+1:-1]
	
	dictt[programname] = timecnt
	#print dictt[programname]
time.close()
ftime = file(sys.argv[2],'a+')
#ftime.write(str(selectedcluster) + "---" + selectedfilename + "---" + str(selectedfileprob) + "\n")
mapping = open(sys.argv[1])
timecnt1 = 0
for line1 in mapping.xreadlines():
	programname1 = line1[:-1]
	timecnt1 += string.atof(dictt[programname1])
	ftime.write(str(timecnt1) + '\n')
mapping.close()
ftime.close()