import horizon

files = set()
error = False

print("# Pool Update")

def cb(st, filename, msg) :
	global error
	if st in (horizon.Pool.UPDATE_STATUS_ERROR, horizon.Pool.UPDATE_STATUS_FILE_ERROR) :
		print(" - ERROR", st, filename, msg)
		error = True
	if st == horizon.Pool.UPDATE_STATUS_FILE :
		files.add(filename)

horizon.Pool.update("pool", cb)

if error :
	exit(1)
else :
	print("okay, %d files "% len(files))
