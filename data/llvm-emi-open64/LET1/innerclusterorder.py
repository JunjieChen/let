import math, random, os, time, shutil, string, sys

dict_prob = open('probability.txt')
dictt={}
for line in dict_prob.xreadlines():
	nPos = line.index(' = ')
	programname = line[:nPos]
	timecnt = line[nPos+3:-1]
	dictt[programname] = timecnt


# for cluster in os.listdir('/SEIDISK/chenjj/compiler/baiyanwei/X-means_2_15_40_che'):
# 	path = os.path.join("/SEIDISK/chenjj/compiler/baiyanwei/X-means_2_15_40_che", cluster)
dir1 = sys.argv[1]

for cluster in os.listdir(dir1):
	path = os.path.join(dir1, cluster)

	# namelist = []
	# problist = []

	dictdict = {}
	if 'cluster' in cluster:
		filecluster = open(path)
		for f in filecluster.xreadlines():
			filename=f[:-1]
			name = filename
			prob = dictt[name]
			# namelist.append(name)
			# problist.append(prob)
			dictdict[name] = string.atof(prob)
		
		
		li = sorted(dictdict.items(), key=lambda d: d[1], reverse=True)


		output = open('./prob/' + str(cluster), 'a')
		print len(li)
		for i in range(0, len(li)):
			output.write(li[i][0])
			output.write(" = ")
			output.write(str(li[i][1]) + '\n')


			#output.write(namelist[problist.index(max(problist))])
			
			#output.write(str(max(problist)) + '\n')
			#namelist.remove(namelist[problist.index(max(problist))])
			#problist.remove(max(problist))
		output.close()	
		filecluster.close()

dict_prob.close()





	# namelist = []
	# problist = []
	# if 'cluster' in cluster:
	# 	filecluster = open(path)
	# 	for f in filecluster.xreadlines():
	# 		filename=f[:-1]
	# 		file_prob = open("probability.txt")
	# 		for line in file_prob.xreadlines():
	# 			if filename in line:
	# 				name = filename
	# 				nPos = line.index('=')
	# 				prob = string.atof(line[nPos + 2:])
	# 				namelist.append(name)
	# 				problist.append(prob)
	# 				break

		# output = open('./prob/' + str(cluster), 'a')
		# print len(namelist)
		# for i in range(0, len(namelist)):
		# 	output.write(namelist[problist.index(max(problist))])
		# 	output.write(" = ")
		# 	output.write(str(max(problist)) + '\n')
		# 	namelist.remove(namelist[problist.index(max(problist))])
		# 	problist.remove(max(problist))
		# output.close()
	#file_prob.close()
