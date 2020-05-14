#!/usr/bin/python3

import argparse
import binascii
import os
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

def check_block_cipher(hexdata):
	if filesize % 8 != 0:
		print("WARNING: This may not be using a block cipher (length of data is not divisible by 8)")
	else:
		print("This might be using a block cipher")
		check_aes(hexdata)

def check_aes(hexdata):
	print("length: %i; mod 8: %i" % (filesize, len(hexdata) % 8))
	if filesize % 16 == 0:
		print("[*] This may be using AES (data length is divisible by 16)")
		print("[*] However, it could be using DES/3DES with an 8 byte block cipher")
	elif filesize % 8 == 0:
		print("[*] Data may be using an 8 byte block cipher using DES/3DES (data length is divisible by 8)")
	else:
		print("[-] Unable to determine potential block cipher")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Read a file in and find repeating hex substrings.')
	parser.add_argument('-f', dest='filename', required=True, help='Filename to parse')
	parser.add_argument('-m', dest='minlength', type=int, default=4, help='minimum length of a hex string to find (default=4)')
	parser.add_argument('-M', dest='maxlength', type=int, default=15, help='maximum length of a hex string to find (default=15)')
	parser.add_argument('-n', dest='minresult', type=int, default=4, help='minimum number of results of substrings found to print (default=4)')
	parser.add_argument('-N', dest='maxresult', type=int, default=15, help='maximum number of results of substrings found to print (default=15)')
	args = parser.parse_args()

	filesize = os.path.getsize(args.filename)
	hexdata = read_file(args.filename)
	check_block_cipher(hexdata)
	substr_counts = find_substrs(args.minlength, args.maxlength)
	filtered_results = filter_results(substr_counts, args.minresult, args.maxresult)
	print_results(filtered_results)

