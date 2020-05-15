#!/usr/bin/python3

import argparse
import binascii
import os
import matplotlib.pyplot as plt

def read_file(filename):
	bytes_dict = {}
	with open(filename,'rb') as f:
		data = f.read(1)
		while data:		# while there are still more bytes being read
			ord_val = ord(data)
			if ord_val not in bytes_dict.keys():
				bytes_dict[ord_val] = 1
			else:
				bytes_dict[ord_val] += 1
			data = f.read(1)
	return bytes_dict

def create_plot(bytes_dict):
	plt.scatter(bytes_dict.keys(), bytes_dict.values())
	plt.xlabel("Hex Byte Character")
	plt.ylabel("No. Of Occurrences")
	plt.title("Entropy Check in %s" % args.filename)
	if args.outputfile:
		print("Writing output to %s" % args.outputfile)
		plt.savefig(args.outputfile)
	else:
		plt.show()

def sort_dict(bytes_dict):
	sorted_dict = {}
	keys = sorted(bytes_dict.keys())
	for key in keys:
		sorted_dict[key] = bytes_dict[key]

	return sorted_dict
		

def print_results(bytes_dict):
	if len(bytes_dict.keys()) > 0:
		#print("=== Filtered Results (Substring Result Count: %i <= n <= %i) ===" % (args.minresult, args.maxresult))
		sorted_dict = sort_dict(bytes_dict)
		for key in sorted_dict:
			print("Byte Value: 0x%02X => %i" % (key, sorted_dict[key]))
	else:
		print("*** No bytes returned ***")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Read a file in and find repeating hex substrings.')
	parser.add_argument('-f', dest='filename', required=True, help='Filename to parse')
	parser.add_argument('-o', dest='outputfile', help='File to write matplot graph output to')
	args = parser.parse_args()

	filesize = os.path.getsize(args.filename)
	bytesdict = read_file(args.filename)
	print_results(bytesdict)
	create_plot(bytesdict)

