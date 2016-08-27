import math, random, os, time, shutil, string,sys

f = file('batch_run.txt', 'a+')
name = 'llvm_dol_gcc'
#for name in os.listdir('/SEIDISK/chenjj/compiler/LET/FSE16/ResultDirChe'):
f.write(name + ',' + '/SEIDISK/chenjj/compiler/LET/FSE16/ResultDirChe/' + name
	+ ',' + name + '1_order.csv' + ',' + name + '1_time.csv'
	+ ',' + name + '2_order.txt' + ',' + name + '2_time.txt'
	+ ',' + name + '3_order.txt' + ',' + name + '3_time.txt'
	+ ',' + name + '4_order.txt' + ',' + name + '4_time.txt'
	+ ',' + name + '5_order.txt' + ',' + name + '5_time.txt'
	+ ',' + name + '6_order.txt' + ',' + name + '6_time.txt'
	+ ',' + name + '7_order.txt' + ',' + name + '7_time.txt'
	+ ',' + name + '8_order.txt' + ',' + name + '8_time.txt'
	+ ',' + name + '9_order.txt' + ',' + name + '9_time.txt'
	+ ',' + name + '10_order.txt' + ',' + name + '10_time.txt'
	+ ',' + 'nonduplicated_order_' + name + '1_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '2_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '3_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '4_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '5_order.txt' 
	+ ',' + 'nonduplicated_order_' + name + '6_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '7_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '8_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '9_order.txt'
	+ ',' + 'nonduplicated_order_' + name + '10_order.txt'
	+ '\n')

f.close()

batch = open('batch_run.txt')

for line in batch.xreadlines():
	linetmp = line[:-1]
	batch_list = linetmp.split(',')
	os.system('mkdir ' + batch_list[0])
	
	os.system('python onlyclassification.py ' + batch_list[2] + ' ' + batch_list[3])
	os.system('python collectResult.py ' + batch_list[2]+' '+sys.argv[1])

	#os.system('python getaverage.py ' + batch_list[22] + ' ' + batch_list[23] + ' ' + batch_list[24] + ' ' + batch_list[25] + ' ' + batch_list[26] + ' ' + batch_list[27] + ' ' + batch_list[28] + ' ' + batch_list[29] + ' ' + batch_list[30] + ' ' + batch_list[31])

	#os.system('python vsrandom.py')

	#os.system('mv average.csv ' + batch_list[0] + '_average.csv')
	os.system('mv *_order.csv ' + batch_list[0])
	os.system('mv *_order.csv ' + batch_list[0])
	os.system('mv *_time.csv ' + batch_list[0])

	#os.system('mv ' + batch_list[0] + '_average.csv ' + batch_list[0])
batch.close()