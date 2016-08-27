import math, random, os, time, shutil, string, sys

dircon='gcc-dol-gcc,gcc-dol-open64,gcc-emi-gcc,gcc-emi-open64,llvm-dol-gcc,llvm-dol-llvm,llvm-dol-open64,llvm-emi-gcc,llvm-emi-llvm,llvm-emi-open64'.split(',')

#gcc-dol-gcc,gcc-dol-open64,gcc-emi-gcc,gcc-emi-open64,llvm-dol-llvm,llvm-dol-open64,llvm-emi-llvm,llvm-emi-open64
result=open('resultAll_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'.csv','w')
for con in dircon:
	tar=open('./'+con+'/LET1/'+con.split('-')[0]+'_'+con.split('-')[1]+'_'+con.split('-')[2]+'/finalresult_'+con.split('-')[0]+'_'+con.split('-')[1]+'_'+con.split('-')[2]+'1_order.csv')
	tarlines=tar.readlines()
	tar.close()

	for i in range(1,len(tarlines)):
		result.write(tarlines[i].strip().split(',')[2]+'\n')

	result.write('\n')
result.close()

file1=open('resultAll_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'.csv')
lines1=file1.readlines()
file1.close()

file2=open('random.csv')
lines2=file2.readlines()
file2.close()

result=open('finalResultAll_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'.csv','w')
for i in range(len(lines2)):
	if lines2[i].strip()=='':
		result.write('\n')
	else:
		result.write(str((float(lines1[i].strip())-float(lines2[i].strip()))/float(lines2[i].strip()))+'\n')
result.close()