import os
import sys
import shutil
from os import listdir
from os.path import isfile, join

print sys.argv
mypath = sys.argv[1]
print mypath
newPath=mypath
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print len(onlyfiles)

for folderIndex in range(0,len(onlyfiles),1000):
	print '-----------------------------'+ str(folderIndex)+ '--------------------------------'
	print '->'+ str(folderIndex+999)
	newPath = mypath+str(folderIndex)+'/'
	try: 
		os.makedirs(newPath)
	except:	
		continue

	for fileIndex in range(folderIndex,folderIndex+999):
		
		if(fileIndex < len(onlyfiles)):
			oldPathFile =mypath+onlyfiles[fileIndex]
			newPathFile = newPath+onlyfiles[fileIndex]
			try: 
				os.rename(oldPathFile, newPathFile)
				shutil.move(oldPathFile,newPathFile)
			except:
				continue
			