import pygit2
import sqlite3
import sys
base = sys.argv[1]

repo = pygit2.Repository("pool")
conn = sqlite3.connect("pool/pool.db")
cur = conn.cursor()

print("# Diff to base")

diff = repo.diff("HEAD", base)
for delta in diff.deltas :
	filename = delta.new_file.path
	cur.execute("SELECT type, name FROM all_items_view WHERE filename=?", (filename,))
	r = cur.fetchone()
	if r is not None :
		print(" - New %s '%s': %s"%(r[0], r[1], filename))
	else:
		print(" - %s not found in pool"%filename)
