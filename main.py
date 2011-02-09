#!/usr/bin/python
import glob
import re

def main ():
	maps = glob.glob('/home/mu/.q3a/q3ut4/*.pk3')
	mapnames = []
	for map in maps:
		m = re.search('(?:.*/)+([^/]+)\\.pk3', map)
		mapnames.append(m.group(1))
	print mapnames


if __name__ == "__main__":	
	main()
