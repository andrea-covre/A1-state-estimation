
'''
	Custom bagfile reader, inspiration from random ros packages.

'''
import rosbag, sys, csv
import time
import string
import os
import shutil 

if (len(sys.argv) > 2):
	print "wrong number of arguments:   " + str(len(sys.argv))
	print "The arguments should be : 'rosbag_csv.py' and 'bagName'"
	sys.exit(1)
elif (len(sys.argv) == 2):
	listOfBagFiles = list(sys.argv(1))
	print "Found 1 bagfile: " + str(listOfBagFiles(0))
elif (len(sys.argv) == 1):
	listOfBagFiles = [b for b in os.listdir(".") if b[-4:] == ".bag"]	
	numberOfFiles = str(len(listOfBagFiles))
	print "reading the" + numberOfFiles + " bagfiles in current directory: \n"
	for bag in listOfBagFiles:
		print bag
	time.sleep(10)
else:
	print "argument error: " + str(sys.argv)	#shouldnt really come up
	sys.exit(1)

count = 0
for bagFile in listOfBagFiles:
	count += 1
	print "reading file " + str(count) + " of  " + numberOfFiles + ": " + bagFile
	#access bag
	bag = rosbag.Bag(bagFile)
	bagContents = bag.read_messages()
	bagName = bag.filename


	#create a new directory
	folder = string.rstrip(bagName, ".bag")
	try:	#else already exists
		os.makedirs(folder)
	except:
		pass
	shutil.copyfile(bagName, folder + '/' + bagName)


	#get list of topics from the bag
	listOfTopics = []
	for topic, msg, t in bagContents:
		if topic not in listOfTopics:
			listOfTopics.append(topic)


	for topic in listOfTopics:
		#Create a new CSV file for each topic
		filename = folder + '/' + string.replace(topic, '/', '_slash_') + '.csv'
		with open(filename, 'w+') as csvfile:
			filewriter = csv.writer(csvfile, delimiter = ',')
			firstIteration = True	#allows header row
			for subtopic, msg, t in bag.read_messages(topic):	# for each instant in time that has data for topicName
				#parse data from this instant, which is of the form of multiple lines of "Name: value\n"
				#	- put it in the form of a list of 2-element lists
				msgString = str(msg)
				msgList = string.split(msgString, '\n')
				instantaneousListOfData = []
				for nameValuePair in msgList:
					splitPair = string.split(nameValuePair, ':')
					for i in range(len(splitPair)):	#should be 0 to 1
						splitPair[i] = string.strip(splitPair[i])
					instantaneousListOfData.append(splitPair)

				if firstIteration:	# header
					headers = ["rosbagTimestamp"]	#first column header
					for pair in instantaneousListOfData:
						headers.append(pair[0])
					filewriter.writerow(headers)
					firstIteration = False

				values = [str(t)]	#first column will have rosbag timestamp
				for pair in instantaneousListOfData:
					print(pair)
					values.append(pair[1])
				filewriter.writerow(values)
	bag.close()
print "Done reading all " + numberOfFiles + " bag files."