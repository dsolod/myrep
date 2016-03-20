import re , sys , os


patterns = (
	('\d{4}-\d\d-\d\d\s\d\d:\d\d:\d\d.+Connected','\d{4}-\d\d-\d\d\s\d\d:\d\d:\d\d.+Disconnected',0),
	('Transaction start','Transaction end',0),
	('Proxying request to','Proxying request to',1),

			)

def findstart(patt, startpos="0"):
	for i in range(startpos)[::-1]:
		if re.search(patterns[patt][0], string[i]):
			return i


def findend(patt, startpos="0"):
	for i in range(startpos, len(string)):
		if re.search(patterns[patt][1], string[i]):
			return i


def savefile(incoming, sdvig=1):
	filik = open(sys.argv[1] + "_.txt", 'w')
	for i in range(len(incoming)):
		for zz in range(incoming[i][0], incoming[i][1] + sdvig):
			x = string[zz] + '\n'
			filik.write(str(x))
		filik.write('*****************\n')

	filik.close()

def mainloop(word, patt):
	print word
	print incoming
	z = 0
	while z < len(string):

		if word in string[z] :
			start = findstart(patt, startpos=z)
			end = findend(patt, startpos=z)
			if start and end:
				incoming.append([start, end])
				z = end

		z += 1


try:

	if os.path.exists(sys.argv[1]) and sys.argv[2]:
		incoming = []
		words = sys.argv[2].split("|")
#		print words
		f = (open(sys.argv[1])).read()
		string = f.split("\n")
		try:
			for xx in words:

				if sys.argv[3].isdigit():
					mainloop(xx, int(sys.argv[3]))
				else:
					print "pattern can be only integer"
				
					
		except IndexError:
			for x in range(len(patterns)):
				print x
				mainloop(xx, x)
		if incoming:

			savefile(incoming)
	else: print "%s does not exist" % sys.argv[1]

except IndexError:
#	print IndexError
	print (
		"####################################################################\n"
		"# you need enter at least file, string, and nubmer.                #\n"
		"# For the example: python pars.py sync.log str X                   #\n"
		"#  where str - string which we serching , x - number of pattern    #\n"
		"# list of pattrens:                                                #\n"
		"####################################################################"
	 	)
	for x in range(len(patterns)):
		print x , patterns[x]
	

#word = "AA_EXPECTED_RECORD_FLAG"  app_server_http_2.log.2
#word = "411bd0f747ff1db0c7ea992a4c348d29"
#print patterns[0]
#print patterns[0][0]
#print range(10)[::-1]