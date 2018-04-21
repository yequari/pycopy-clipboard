#! python3
# pw.py - the worst password locker ever

DIRECTORY = 'F:\\Python\\scripts' # Folder clipboard file is kept in
FILENAME = 'clipboard.txt' # Name of clipboard file
TEXT = {}

import sys, pyperclip, os

os.chdir(DIRECTORY)
clipFile = open(FILENAME)

clipData = clipFile.readlines()
for index, line in enumerate(clipData):
	clipData[index] = line.strip()
	currLine = line.split(" :: ")
	TEXT.setdefault(currLine[0], '')
	TEXT[currLine[0]] = currLine[1]

clipFile.close()

if len(sys.argv) < 2:
	print("Usage: py pycopy.py [key] - copy value by key")
	sys.exit()

key = sys.argv[1]

if key in TEXT:
	pyperclip.copy(TEXT[key])
	print("Text entry for " + key + " copied to clipboard")
	#print(TEXT[key])
else:
	print("There is no key named " + key)