# pwned
Python script to check if your password was pwned using sha1 hashes from site https://haveibeenpwned.com/

The files for V2 of the database are sorted by number of usages, not by hash.
So we either need to do this ourselves:

```
sort --parallel=7 -S 60G -o pwned-passwords-2.0_sorted.txt -T .  < pwned-passwords-2.0.txt
```
Or you can use the torrent available here via [magnet link](magnet:?xt=urn:btih:5fcbad0f19a83b01512302430bcfa7bad5b8edd9&dn=pwned-passwords-2.0_sorted.txt.7z&tr=udp%3a%2f%2ftracker.zer0day.to%3a1337%2fannounceee7&tr=udp%3a%2f%2f9.rarbg.com%3a2750%2fannounceel33&tr=udp%3a%2f%2f9.rarbg.com%3a2750%2fannounce31&tr=http%3a%2f%2ftracker.vanitycore.co%3a6969%2fannounceel38&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounceel35&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounceel46&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounceel41&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce36&tr=udp%3a%2f%2ftracker.vanitycore.co%3a6969%2fannounce42&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounceel31&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounceel44&tr=udp%3a%2f%2fp4p.arenabg.ch%3a1337%2fannounceel44&tr=udp%3a%2f%2fannounce.torrentsmd.com%3a8080%2fannounceel43&tr=udp%3a%2f%2ftracker1.wasabii.com.tw%3a6969%2fannounceel41&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce43&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounceel34&tr=udp%3a%2f%2ftracker.dler.org%3a6969%2fannounceel32&tr=udp%3a%2f%2fmgtracker.org%3a2710%2fannounceel42&tr=http%3a%2f%2fmgtracker.org%3a2710%2fannounce33&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=http%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce35&tr=http%3a%2f%2fannounce.torrentsmd.com%3a8080%2fannounce43&tr=http%3a%2f%2fp4p.arenabg.ch%3a1337%2fannounce34&tr=http%3a%2f%2facademictorrents.com%2fannounce.php&tr=http%3a%2f%2fannounce.torrentsmd.com%3a6969%2fannounce43&tr=http%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce40&tr=udp%3a%2f%2fannounce.torrentsmd.com%3a6969%2fannounce44&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounceel36)


First of all you have to download password files from this site https://haveibeenpwned.com/Passwords.
Since they're huge, use torrent for this if you can. Then uzip files.

For tis command, it's important to control...

* the temporary folder: `-T .` puts `sort`'s temporary files into the current folder. I do this since for my machines `/tmp` tends to be too small
* the number of cores used for sorting: `--parallel=7` uses all but one core on my 8 core machine. No use waiting longer than necessary.
* the amound of memory to use: `-S 60G` tells `sort` to use up to 60 GiB of memory! If you can, make this huge, since otherwise `sort` will have to write/read a lot of temporary files.

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

[1]: magnet:?xt=urn:btih:5fcbad0f19a83b01512302430bcfa7bad5b8edd9&dn=pwned-passwords-2.0_sorted.txt.7z&tr=udp%3a%2f%2ftracker.zer0day.to%3a1337%2fannounceee7&tr=udp%3a%2f%2f9.rarbg.com%3a2750%2fannounceel33&tr=udp%3a%2f%2f9.rarbg.com%3a2750%2fannounce31&tr=http%3a%2f%2ftracker.vanitycore.co%3a6969%2fannounceel38&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounceel35&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounceel46&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounceel41&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce36&tr=udp%3a%2f%2ftracker.vanitycore.co%3a6969%2fannounce42&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounceel31&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounceel44&tr=udp%3a%2f%2fp4p.arenabg.ch%3a1337%2fannounceel44&tr=udp%3a%2f%2fannounce.torrentsmd.com%3a8080%2fannounceel43&tr=udp%3a%2f%2ftracker1.wasabii.com.tw%3a6969%2fannounceel41&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce43&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounceel34&tr=udp%3a%2f%2ftracker.dler.org%3a6969%2fannounceel32&tr=udp%3a%2f%2fmgtracker.org%3a2710%2fannounceel42&tr=http%3a%2f%2fmgtracker.org%3a2710%2fannounce33&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=http%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce35&tr=http%3a%2f%2fannounce.torrentsmd.com%3a8080%2fannounce43&tr=http%3a%2f%2fp4p.arenabg.ch%3a1337%2fannounce34&tr=http%3a%2f%2facademictorrents.com%2fannounce.php&tr=http%3a%2f%2fannounce.torrentsmd.com%3a6969%2fannounce43&tr=http%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce40&tr=udp%3a%2f%2fannounce.torrentsmd.com%3a6969%2fannounce44&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounceel36
