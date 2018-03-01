# pwned
Python script to check if your password was pwned using sha1 hashes from site https://haveibeenpwned.com/

The files for V2 of the database are sorted by number of usages, not by hash.
So we either need to do this ourselves or you can use the torrent available here [here](https://downloads.pwnedpasswords.com/passwords/pwned-passwords-ordered-2.0.txt.7z.torrent). Be nice and keep seeding :)

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

It will be very fast even on the 30G password file.
