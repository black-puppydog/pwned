#!python3.6

import os
import sys
import hashlib
import collections
from getpass import getpass

SearchResult = collections.namedtuple('SearchResult', ['lineno', 'used', 'tries', 'sha1hash'])
def check_passwd(filename, passwd):
    file_size = os.stat(filename).st_size
    found = False
    tries = 0

    lines = file_size // RECORD_SIZE
    print(f'number of entries: {lines}')
    low = 0
    high = lines
    mid = (low + high) // 2

    with open(filename, 'rb') as psfile:
        while low <= high:
            tries += 1
            mid = (low + high) // 2
            psfile.seek(mid * RECORD_SIZE)
            entry, used = psfile.read(RECORD_SIZE - 1).strip().split(b':')
            entry = entry.decode('ascii')
            used = int(used.decode('ascii'))

            if passwd < entry:
                high = mid - 1
            elif passwd > entry:
                low = mid + 1
            elif passwd == entry:
                return SearchResult(lineno=mid+1, tries=tries, sha1hash=entry, used=used)
    return None


def check_password_and_show_result(filename, password):
    result = check_passwd(filename, password)
    if result is None:
        print("Password was not found")
    else:
        print('Password found on line %d used %d times.\t hash %s tries %d' % (
            result.lineno, result.used, result.sha1hash, result.tries))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Using pwned-passwords-2.0_sorted.txt by default')
        filename = 'pwned-passwords-2.0_sorted.txt'
    else:
      filename = sys.argv[1]
    global RECORD_SIZE
    with open(filename, 'rb') as psfile:
        RECORD_SIZE = len(psfile.readline())
    ps = getpass('enter your password: ')
    passwd_orig = hashlib.sha1(ps.encode('utf-8')).hexdigest().upper()
    passwd_lower = hashlib.sha1(ps.lower().encode('utf-8')).hexdigest().upper()
    passwd_upper = hashlib.sha1(ps.upper().encode('utf-8')).hexdigest().upper()
    print('Original password hash: %s\nYour lower password hash: %s\nupper password hash: %s' % (
        passwd_orig, passwd_lower, passwd_upper))

    print("\nSearch original password")
    result = check_password_and_show_result(filename, passwd_orig)

    print("\nSearch upper case password")
    result = check_password_and_show_result(filename, passwd_upper)

    print("\nSearch lower case password")
    check_password_and_show_result(filename, passwd_lower)
