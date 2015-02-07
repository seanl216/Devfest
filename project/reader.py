def make_havens(filename):
	"""Create list of haven, saved as dictionaries"""
	haven_file = open(filename, 'r')
	havens = []
	line = haven_file.readline()
	while line != '':
		haven = make_haven(line)
		if haven != None:
			havens.append(haven)
		line = haven_file.readline()
	return havens

def make_haven(line):
	"""Return a haven, saved as a dictionary"""
	info = line.split('\t')
	haven = {}
	haven['name'] = info[0]
	s = len(info)
	if s > 1:
		if info[1] != '':
			haven['address'] = info[1]
			return haven