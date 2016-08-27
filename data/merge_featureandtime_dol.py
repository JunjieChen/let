import os
import os.path
import subprocess as subp
import sys
import thread
import time

dircon='gcc-dol-gcc,gcc-dol-open64,llvm-dol-gcc,llvm-dol-llvm,llvm-dol-open64'.split(',')

#,gcc-emi-gcc,gcc-emi-open64,llvm-emi-gcc,llvm-emi-llvm,llvm-emi-open64

for con in dircon:
	os.chdir('./'+con)
	os.system('cp ../feature_time_training.csv .')
	f=open('feature_time_training.csv')
	lf=f.readlines()
	f.close()

	t=open('trainingtime.txt')
	lt=t.readlines()
	t.close()


	data=dict()
	for i in range(len(lt)):
		tmp=lt[i].strip().split(',')[0][7:-2]
		data[tmp]=str(float(lt[i].strip().split(',')[-1]))

	result=open('time_trainingset.csv','w')
	a=[]
	for i in range(1,419):
		a.append(str(i))
	result.write(','.join(a)+'\n')
	for i in range(1,len(lf)):
		result.write(lf[i].strip()+','+data[str(i)]+'\n')

	result.close()

	os.system('rm feature_time_training.csv')

	os.chdir('../')
