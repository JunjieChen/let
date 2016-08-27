import math, random, os, time, shutil, string, sys

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
list10=[]

list11=[]
list21=[]
list31=[]
list41=[]
list51=[]
list61=[]
list71=[]
list81=[]
list91=[]
list101=[]

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])
file3 = open(sys.argv[3])
file4 = open(sys.argv[4])
file5 = open(sys.argv[5])
file6 = open(sys.argv[6])
file7 = open(sys.argv[7])
file8 = open(sys.argv[8])
file9 = open(sys.argv[9])
file10 = open(sys.argv[10])

for linetime1 in file1.xreadlines():
	pos1 = linetime1.index(',')
	pos11 = linetime1[pos1 + 1:].index(',')
	list1.append(string.atof(linetime1[:pos1]))
	linetime11 = linetime1[pos1 + 1:]
	list11.append(string.atof(linetime11[pos11 + 1:-1]))

for linetime2 in file2.xreadlines():
	pos2 = linetime2.index(',')
	list2.append(string.atof(linetime2[:pos2]))
	pos21 = linetime2[pos2 + 1:].index(',')
	linetime21 = linetime2[pos2 + 1:]
	list21.append(string.atof(linetime21[pos21 + 1:-1]))


for linetime3 in file3.xreadlines():
	pos3 = linetime3.index(',')
	list3.append(string.atof(linetime3[:pos3]))
	pos31 = linetime3[pos3 + 1:].index(',')
	linetime31 = linetime3[pos3 + 1:]
	list31.append(string.atof(linetime31[pos31 + 1:-1]))

for linetime4 in file4.xreadlines():
	pos4 = linetime4.index(',')
	list4.append(string.atof(linetime4[:pos4]))
	pos41 = linetime4[pos4 + 1:].index(',')
	linetime41 = linetime4[pos4 + 1:]
	list41.append(string.atof(linetime41[pos41 + 1:-1]))

for linetime5 in file5.xreadlines():
	pos5 = linetime5.index(',')
	list5.append(string.atof(linetime5[:pos5]))
	pos51 = linetime5[pos5 + 1:].index(',')
	linetime51 = linetime5[pos5 + 1:]
	list51.append(string.atof(linetime51[pos51 + 1:-1]))

for linetime6 in file6.xreadlines():
	pos6 = linetime6.index(',')
	list6.append(string.atof(linetime6[:pos6]))
	pos61 = linetime6[pos6 + 1:].index(',')
	linetime61 = linetime6[pos6 + 1:]
	list61.append(string.atof(linetime61[pos61 + 1:-1]))

for linetime7 in file7.xreadlines():
	pos7 = linetime7.index(',')
	list7.append(string.atof(linetime7[:pos7]))
	pos71 = linetime7[pos7 + 1:].index(',')
	linetime71 = linetime7[pos7 + 1:]
	list71.append(string.atof(linetime71[pos71 + 1:-1]))

for linetime8 in file8.xreadlines():
	pos8 = linetime8.index(',')
	list8.append(string.atof(linetime8[:pos8]))
	pos81 = linetime8[pos8 + 1:].index(',')
	linetime81 = linetime8[pos8 + 1:]
	list81.append(string.atof(linetime81[pos81 + 1:-1]))

for linetime9 in file9.xreadlines():
	pos9 = linetime9.index(',')
	list9.append(string.atof(linetime9[:pos9]))
	pos91 = linetime9[pos9 + 1:].index(',')
	linetime91 = linetime9[pos9 + 1:]
	list91.append(string.atof(linetime91[pos91 + 1:-1]))

for linetime10 in file10.xreadlines():
	pos10 = linetime10.index(',')
	list10.append(string.atof(linetime10[:pos10]))
	pos101 = linetime10[pos10 + 1:].index(',')
	linetime101 = linetime10[pos10 + 1:]
	list101.append(string.atof(linetime101[pos101 + 1:-1]))

number = 1
f = file('average.csv','a+')
for i in range(0, len(list101)):
	r1 = (list1[i] + list2[i] + list3[i] + list4[i] + list5[i] + list6[i] + list7[i] + list8[i] + list9[i] + list10[i])/10
	f.write(str("%.0f"%r1) + ',' + str(number) +',' + str((list11[i] + list21[i] + list31[i] + list41[i] + list51[i] + list61[i] + list71[i] + list81[i] + list91[i] + list101[i])/10) + '\n')
	number += 1
f.close()

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()