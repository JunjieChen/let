In the package, each folder represents each setting. For example, gcc-dol-open64: gcc represents the subject used in the scheduling process; dol represents the accelerated compiler testing technique; open64 represents the subjects used in the learning process. Next, I explain the files in each folder and I use the folder gcc-dol-open64 as the representative, and other folders are as similar as it.

In the folder gcc-dol-open64: 

There are several main files as follows:
yes_1000_no_1000_times_selected.csv: the training set for training a capability model
feature_filter_selected: the testing set for predicting the bug-revealing probability of each new test program
time_trainingset: the training set for training a time model
feature_filter_testtime: the testing set for predicting the execution time of each new test program
probability.txt: the predicted bug-revealing probabilities of new test programs
predictedtime.txt: the predicted execution time of new test programs
prob_per.csv: the bug-revealing probabilities in unit time of new test programs
./LET/gcc_dol_open64/prob_order.csv: the execution order of new test programs scheduled by LET
./LET/gcc_dol_open64/finalresult_gcc_dol_open641_order.csv: the results of detecting bugs

The other files are intermediate output files


In the package, there are some files not in those folders, and then I explain them in detail.

trainModel.py: the main source code file of LET and it will call some other source code files
Trainingset.java: the source code of training a capability model
train.java: the source code of training a time model
Classify_1.java: the source code of predicting the bug-revealing probabilities of new test programs
test.java: the source code of predicting the execution time of new test programs
resultAll_1.0_3.3_0.5.csv: the time spent on detecting bugs in all settings
finalResultAll_1.0_3.3_0.5.csv: the speedups for detecting bugs in all settings

In particular, in resultAll_1.0_3.3_0.5.csv and finalResultAll_1.0_3.3_0.5.csv, the result order are: gcc-dol-gcc, gcc-dol-open64, gcc-emi-gcc, gcc-emi-open64, llvm-dol-gcc, llvm-dol-llvm, llvm-dol-open64, llvm-emi-gcc, llvm-emi-llvm, llvm-emi-open64


Furthermore, if you want to reproduce our experiments, you can easily run the following instruction:

		python trainModel.py 1.0 0.7 3.3 0.5

by using this instruction, you can directly acquire all the experiemnts results of LET, and 1.0 and 0.7 are parameters for training a capability model and 3.3 and 0.5 are parameters for training a time model.


Thanks
