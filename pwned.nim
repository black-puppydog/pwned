import os
import securehash
import strutils
import unicode

const RECORD_SIZE:int = 42
proc check_passwd(filename, passwd: string): bool =
    let
        file_size = os.getFileSize(filename)
        passwd_file = open(filename, fmRead)
    var
        tries: int64 = 0
        min: int64 = 0
        max: int64 = file_size div RECORD_SIZE
        mid: int64 = (min + max) div 2
        line = newString(40)
    
    while min <= max:
        tries += 1
        mid = (min + max) div 2
        passwd_file.setFilePos(mid * RECORD_SIZE)
        discard passwd_file.readChars(line, 0, 40)
        if passwd > line:
            min = mid + 1
        elif passwd < line:
            max = mid - 1
        elif passwd == line:
            echo("Found line $1\npos $2\ntries $3" % [$line, $mid, $tries])
            return true
    return false



when isMainModule:
    if paramCount() < 1:
        quit "You have to supply password file"
    stdout.write("enter your password: ")
    let
        filename = paramStr(1)
        passwd = stdin.readLine
        passwd_lower = secureHash(unicode.toLower(passwd))
        passwd_upper = secureHash(unicode.toUpper(passwd))
    echo("Your lower password hash: $1\nupper password hash: $2" % [$passwd_lower, $passwd_upper])
    if not check_passwd(filename, $passwd_lower):
        echo("Lower passwd NOT found")
    
    if not check_passwd(filename, $passwd_upper):
        echo("Upper passwd NOT found")
