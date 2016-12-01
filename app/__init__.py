import hashlib, msgpack

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def calculate_checksums(file_name):
    md5_obj = hashlib.md5()
    sha1_obj = hashlib.sha1()
    with open(file_name, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5_obj.update(data)
            sha1_obj.update(data)

    return [md5_obj, sha1_obj]


def hash_file(file_path, hash_type="both"):
    [md5, sha1] = calculate_checksums(file_path)

    target = open(file_path + get_hash_extension(hash_type), 'w')
    target.truncate()

    sha1 = sha1.hexdigest()
    md5 = md5.hexdigest()

    if hash_type == "md5":
        target.write(md5)
    elif hash_type == "sha1":
        target.write(sha1)
    else:
        target.write(msgpack.packb({
            "sha1": sha1,
            "md5": md5,
        }))

    target.close()


def get_hash_extension(hash_type):
    if hash_type == "md5":
        return '.md5'
    elif hash_type == "sha1":
        return '.sha1'
    else:
        return '.ph'
