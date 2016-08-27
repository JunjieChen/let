import os
import os.path
import subprocess as subp
import sys
import thread
import time

dircon='gcc-dol-gcc,gcc-dol-open64,gcc-emi-gcc,gcc-emi-open64,llvm-dol-gcc,llvm-dol-llvm,llvm-dol-open64,llvm-emi-gcc,llvm-emi-llvm,llvm-emi-open64'.split(',')
#,gcc-dol-open64,gcc-emi-gcc,gcc-emi-open64,llvm-dol-gcc,llvm-dol-llvm,llvm-dol-open64,llvm-emi-gcc,llvm-emi-llvm,llvm-emi-open64
for con in dircon:
	os.chdir('./'+con)
	sumtime=0.0
	# training the model to predict probabilities

	os.system('rm SMO.model')
	os.system('rm Gaussian.model')
	os.system('rm Trainingset.class')
	os.system('rm predictedtime.txt')
	os.system('rm prob_per.txt')
	
	os.system('cp ../Trainingset.java .')
	os.system('cp ../weka.jar .')

	os.system('javac -classpath .:weka.jar Trainingset.java')
	os.system('java -cp .:weka.jar Trainingset '+sys.argv[1]+' '+sys.argv[2])
	
	result=open('Time_probability.txt','w')

	os.system('rm probability.txt')
	os.system('rm Classify_1.class')
	
	os.system('cp ../Classify_1.java .')
	os.system('javac -classpath .:weka.jar Classify_1.java')
	begin=time.time()
	os.system('java -cp .:weka.jar Classify_1')
	end=time.time()
	sumtime+=(end-begin)
	result.write('predict probability: '+str(end-begin)+'\n')
	result.close()
	
	os.system('rm Classify_1.java')
	os.system('rm Classify_1.class')

	os.system('rm Trainingset.java')
	os.system('rm Trainingset.class')
	
	#training the model to predict the execution time
	
	os.system('cp ../train.java .')
	os.system('javac -classpath .:weka.jar train.java')
	os.system('java -cp .:weka.jar train '+sys.argv[3]+' '+sys.argv[4])

	os.system('rm train.java')
	os.system('rm train.class')

	f418=open('feature_filter.csv')
	l418=f418.readlines()
	f418.close()

	r418=open('feature_filter_testtime.csv','w')
	for i418 in range(len(l418)):
		if i418==0:
			r418.write(l418[i418].strip()+',418\n')
		else:
			r418.write(l418[i418].strip()+',0\n')
	r418.close()

	os.system('cp ../test.java .')
	os.system('javac -classpath .:weka.jar test.java')
	result=open('Time_predicttime.txt','w')
	begin=time.time()
	os.system('java -cp .:weka.jar test')
	end=time.time()
	sumtime+=(end-begin)
	result.write('predict execution time: '+str(end-begin)+'\n')
	result.close()

	os.system('rm test.java')
	os.system('rm test.class')
	
	#calculat probability/time
	result=open('Time_calculation.txt','w')
	begin=time.time()
	probfile=open('probability.txt')
	problines=probfile.readlines()
	probfile.close()

	timefile=open('predictedtime.txt')
	timelines=timefile.readlines()
	timefile.close()

	probperfile=open('prob_per.csv','w')
	for prob_i in range(len(problines)):
		if timelines[prob_i].strip().split(' = ')[-1]=='0':
			probperfile.write(problines[prob_i].strip().split(' = ')[0]+' = '+str(float(problines[prob_i].strip().split(' = ')[-1])/0.000001)+'\n')
		else:
			probperfile.write(problines[prob_i].strip().split(' = ')[0]+' = '+str(float(problines[prob_i].strip().split(' = ')[-1])/float(timelines[prob_i].strip().split(' = ')[-1]))+'\n')
	probperfile.close()

	end=time.time()
	sumtime+=(end-begin)
	result.write('calculate probability/time: '+str(end-begin)+'\n')
	result.close()

	#ranking test cases
	os.chdir('./LET1')
	os.system('rm -rf '+con.split('-')[0]+'_'+con.split('-')[1]+'_'+con.split('-')[2])
	os.system('rm -rf batch_run.txt')
	os.system('cp ../prob_per.csv .')
	os.system('python batch.py '+str(sumtime))

	os.system('rm prob_per.csv')
	os.chdir('../')

	os.chdir('../')
os.system('python getResult.py '+sys.argv[1]+' '+sys.argv[3]+' '+sys.argv[4])