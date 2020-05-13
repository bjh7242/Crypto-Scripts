#!/usr/bin/python3

import argparse
import binascii
import pprint
from itertools import combinations

def read_file(filename):
	with open(filename,'rb') as f:
		data = f.read()
	hexdata = binascii.hexlify(data).decode()
	return hexdata

def get_substr():
	for x, y in combinations(range(len(hexdata) + 1), r = 2):
		yield hexdata[x:y]


def find_substrs(minlength, maxlength):
	substr_counts = {}
	print("Finding substrings... this may take a bit...")

	for substr in get_substr():
		if len(substr) >= minlength and len(substr) <= maxlength:
			if substr in substr_counts.keys():
				print("Found existing substr: %s" % substr)
				substr_counts[substr] += 1
			else:
				substr_counts[substr] = 1

	return substr_counts

def filter_results(substr_dict, minresult, maxresult):
	filtered_results = {}
	for key in substr_dict:
		if substr_dict[key] >= minresult and substr_dict[key] <= maxresult:
			filtered_results[key] = substr_dict[key]

	return filtered_results

def print_results(filtered_results):
	if len(filtered_results.keys()) > 0:
		print("=== Filtered Results (Substring Result Count: %i <= n <= %i) ===" % (args.minresult, args.maxresult))
		for key in filtered_results:
			print("Sub string: %s => %i" % (key, filtered_results[key]))
	else:
		print("*** No results matching min/max results for substrings***")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Read a file in and find repeating hex substrings.')
	parser.add_argument('-f', dest='filename', required=True, help='Filename to parse')
	parser.add_argument('-m', dest='minlength', type=int, default=4, help='minimum length of a hex string to find')
	parser.add_argument('-M', dest='maxlength', type=int, default=15, help='maximum length of a hex string to find')
	parser.add_argument('-n', dest='minresult', type=int, default=4, help='minimum number of results of substrings found to print')
	parser.add_argument('-N', dest='maxresult', type=int, default=15, help='maximum number of results of substrings found to print')

	args = parser.parse_args()
	hexdata = read_file(args.filename)
	substr_counts = find_substrs(args.minlength, args.maxlength)
	filtered_results = filter_results(substr_counts, args.minresult, args.maxresult)
	print_results(filtered_results)

