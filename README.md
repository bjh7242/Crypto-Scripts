# Detect_ECB
This script is meant to detect whether or not a file is encrypted with a block cipher using an ECB mode

To generate an encrypted file using DES-ECB:
```bash
openssl enc -des-ecb -K e0e0e0e0f1f1f1f1 -in /bin/ls -out ls.enc
```


