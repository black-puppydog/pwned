import os
import sys
import hashlib
import collections

RECORD_SIZE = 42
SearchResult = collections.namedtuple('SearchResult', ['lineno', 'tries', 'sha1hash'])
def check_passwd(filename, passwd):
    file_size = os.stat(filename).st_size
    found = False
    tries = 0
    
    lines = file_size // RECORD_SIZE
    low = 0
    high = lines
    mid = (low + high) // 2

    with open(filename, 'r', encoding='utf-8') as psfile:
        while low <= high:
            tries += 1
            mid = (low + high) // 2
            psfile.seek(mid * RECORD_SIZE)
            line = psfile.read(RECORD_SIZE - 1)
            line = line.strip()

            if int(passwd, 16) < int(line, 16):
                high = mid - 1 
            elif int(passwd, 16) > int(line, 16):
                low = mid + 1
            elif int(passwd, 16) == int(line, 16):
                return SearchResult(lineno=mid+1, tries=tries, sha1hash=line)
    return None


def check_password_and_show_result(filename, password):
    result = check_passwd(filename, password)
    if result is None:
        print("Password was not found")
    else:
        print('Password found on line %d hash %s tries %d' % (
            result.lineno, result.sha1hash, result.tries))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You have to supply password file.")
        sys.exit(1)

    filename = sys.argv[1]
    ps = input('enter your password: ')
    passwd_lower = hashlib.sha1(ps.lower().encode('utf-8')).hexdigest().upper()
    passwd_upper = hashlib.sha1(ps.upper().encode('utf-8')).hexdigest().upper()
    print('Your lower password hash: %s\nupper password hash: %s' % (
        passwd_lower, passwd_upper))
    
    print("\nSearch upper case password")
    result = check_password_and_show_result(filename, passwd_upper)

    print("\nSearch lower case password")
    check_password_and_show_result(filename, passwd_lower)
