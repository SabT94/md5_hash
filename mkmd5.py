import hashlib
import os,sys

def getHash(path, blocksize=65536):
	f = open(path,'rb')
	hasher = hashlib.md5()
	buf = f.read(blocksize)
	while len(buf)>0:
		hasher.update(buf)
		buf = f.read(blocksize)
	f.close()
	return hasher.hexdigest()

file = sys.argv[1]

if os.path.exists(file):
	fileHash = getHash(file)
	print(fileHash)
else:
	print('%s is not a valid path, please verity'%file)
	sys.exit()




