# Crypto Scripts

## Detect ECB
This script is meant to detect whether or not a file is encrypted with a block cipher using an ECB mode. 
Since ECB mode block ciphers use a repeating key, there is a potential that you will see repeating ciphertext. 
This script will read in a file and search the hex characters of the file for repeating values. 
The parameters for searching are configurable (minimum/maximum string length, and minimum/maximum amount a string shows up in the file).

### Usage
```bash
user@localhost:~$ python3 detect_ecb.py -h
usage: detect_ecb.py [-h] -f FILENAME [-m MINLENGTH] [-M MAXLENGTH]
                     [-n MINRESULT] [-N MAXRESULT]

Read a file in and find repeating hex substrings.

optional arguments:
  -h, --help    show this help message and exit
  -f FILENAME   Filename to parse
  -m MINLENGTH  minimum length of a hex string to find (default=4)
  -M MAXLENGTH  maximum length of a hex string to find (default=15)
  -n MINRESULT  minimum number of results of substrings found to print
                (default=4)
  -N MAXRESULT  maximum number of results of substrings found to print
                (default=15)
```

To search a given file **$FILE** for repeating strings and only print results if there is a minimum of 5 results for that string found in a file:
```
python3 detect_ecb.py -f $FILE -n 5
```

To further filter your results, you may add a minimum length of characters for a substring to search for (ex. search for substrings with a minimum length of 5 characters):
```
python3 detect_ecb.py -f $FILE -n 5 -m 5
```

## Entropy Check
To check the entropy of a file (and create a graph of the number of occurences of 8 byte values in a given file), you can use `entropy_check.py`. 
To determine if something is properly encrypted, the number of occurences of each byte should be roughly the same, otherwise any outliers can show a bias in the encryption algorithm.

### Usage
```bash
user@localhost:~$ python3 entropy_check.py -h
usage: entropy_check.py [-h] -f FILENAME [-o OUTPUTFILE]

Read a file in and find repeating hex substrings.

optional arguments:
  -h, --help     show this help message and exit
  -f FILENAME    Filename to parse
  -o OUTPUTFILE  File to write matplot graph output to
```

To parse file **$FILE** and write the graph output to **OUTPUT.png** 
```
python3 entropy_check.py -f $FILE -o OUTPUT.png
```

## Test File Encryption
To generate an encrypted file using DES-ECB:

```bash
openssl enc -des-ecb -K e0e0e0e0f1f1f1f1 -in /bin/ls -out ls.enc
```


