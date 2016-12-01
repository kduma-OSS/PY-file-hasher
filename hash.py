#!/usr/bin/python

import app, sys, os.path, argparse

parser = argparse.ArgumentParser(description='File Hasher.')

parser.add_argument(
    'files',
    metavar='file',
    nargs='+',
    help='files to be hashed'
)

parser.add_argument(
    '-t',
    '--type',
    dest='hash_type',
    default='both',
    help='type of hash (default: both)',
    choices=['both', 'md5', 'sha1']
)

args = parser.parse_args()

for filename in args.files:
    if filename[-3:] == ".ph" or filename[-5:] == ".sha1" or filename[-4:] == ".md5":
        continue

    if not os.path.isfile(filename):
        continue

    app.hash_file(filename, hash_type=args.hash_type)

    print filename + " Hashed!"
