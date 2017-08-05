# pwned
Python script to check if your password was pwned using sha1 hashes from site https://haveibeenpwned.com/

First of all you have to download password files from this site https://haveibeenpwned.com/Passwords. Then uzip files.

clone this repo
```
git clone https://github.com/cyberlis/pwned.git
cd pwned
```

To check if you password was compromised run this command:
```
python3 pwned.py <path_to_password_file>
```
Example
```
python3 pwned.py pwned-passwords-1.0.txt
```

Program will ask your password and after that it will check this password using binary search algorithm.

It will be very fast even on 12G password file