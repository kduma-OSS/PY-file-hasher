# PY-file-hasher
MD5 and SHA1 file hash calculator and checker

## hasher
```
usage: hash [-h] [-t {both,md5,sha1}] file [file ...]

File Hasher.

positional arguments:
  file                  files to be hashed

optional arguments:
  -h, --help            show this help message and exit
  -t {both,md5,sha1}, --type {both,md5,sha1}
                        type of hash (default: both)
```

## checker
```
usage: check [-h] [-g] file [file ...]

File Hash Checker.

positional arguments:
  file        files to be checked

optional arguments:
  -h, --help  show this help message and exit
  -g, --gui   sum the integers (default: find the max)
```
