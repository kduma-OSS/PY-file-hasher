#!/usr/bin/python

import msgpack, app, sys, os.path, argparse
from Tkinter import *
import ttk

parser = argparse.ArgumentParser(description='File Hash Checker.')

parser.add_argument(
    'files',
    metavar='file',
    nargs='+',
    help='files to be checked'
)

parser.add_argument(
    '-g',
    '--gui',
    dest='gui',
    default=False,
    action='store_true',
    help='sum the integers (default: find the max)'
)

args = parser.parse_args()

if args.gui:
    root = Tk(screenName="Sprawdzanie sum kontrolnych!")
    root.wm_title("Hello, world")

    tree = ttk.Treeview(root)
    tree.pack(fill=BOTH, expand=YES)

    tree["columns"] = ("sha1", "md5")
    tree.column("sha1", width=150)
    tree.column("md5", width=150)
    tree.heading("sha1", text="SHA1")
    tree.heading("md5", text="MD5")

for filename in args.files:

    if not os.path.isfile(filename):
        continue

    with open(filename, 'r') as sig_file:
        sig = sig_file.read()

    md5 = False
    sha1 = False

    if filename[-3:] == ".ph":
        hashed_file = filename[:-3]
        sig = msgpack.unpackb(sig)
        md5 = sig['md5']
        sha1 = sig['sha1']
    elif filename[-5:] == ".sha1":
        hashed_file = filename[:-5]
        sha1 = sig
    elif filename[-4:] == ".md5":
        hashed_file = filename[:-4]
        md5 = sig
    else:
        continue

    if not os.path.isfile(hashed_file):
        print hashed_file + " FILE DOESNT EXISTS!"
        continue

    [calculated_md5, calculated_sha1] = app.calculate_checksums(hashed_file)

    print "\nFile '" + hashed_file + "':"

    tag = 'success'

    if md5:
        if calculated_md5.hexdigest() == md5:
            print app.bcolors.OKGREEN + "\tMD5 hash is valid!" + app.bcolors.ENDC
            md5 = 1
        else:
            print app.bcolors.FAIL + "\tMD5 hash is INVALID!" + app.bcolors.ENDC
            tag = 'error'
            md5 = -1
    else:
        print app.bcolors.OKBLUE + "\tMD5 check skipped" + app.bcolors.ENDC
        md5 = 0

    if sha1:
        if calculated_sha1.hexdigest() == sha1:
            print app.bcolors.OKGREEN + "\tSHA1 hash is valid!" + app.bcolors.ENDC
            sha1 = 1
        else:
            print app.bcolors.FAIL + "\tSHA1 hash is INVALID!" + app.bcolors.ENDC
            tag = 'error'
            sha1 = -1
    else:
        print app.bcolors.OKBLUE + "\tSHA1 check skipped" + app.bcolors.ENDC
        sha1 = 0

    if args.gui:
        tree.insert(
            "",
            0,
            text=os.path.basename(filename[:-4]),
            values=(
                ("OK!" if sha1 == 1 else "-" if sha1 == 0 else "BLAD SUMY KONTROLNEJ"),
                ("OK!" if md5 == 1 else "-" if md5 == 0 else "BLAD SUMY KONTROLNEJ"),
            ),
            tags=(tag)
        )


if args.gui:
    tree.tag_configure('warning', background='orange')
    tree.tag_configure('error', background='red')
    tree.tag_configure('success', background='green')
    tree.pack()
    root.minsize(width=900, height=500)
    root.mainloop()
