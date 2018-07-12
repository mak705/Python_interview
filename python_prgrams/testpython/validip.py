def valid_ip(address):
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False
print valid_ip('266.10.20.30')

---------------

def ipcheck():
    input_ip = raw_input('Enter the ip:')
    flag = 0
    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
    match = re.match(pattern, input_ip)
    if (match):
        field = input_ip.split(".")
        for i in range(0, len(field)):
            if (int(field[i]) < 256):
                flag += 1
            else:
                flag = 0
    if (flag == 4):
        print("valid ip")
    else:
        print('No match for ip or not a valid ip')

-------------------------------------

import re
hostIP = '290.168.1.5'
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
test = pat.match(hostIP)
if (test):
   print "Acceptable ip address"
else:
   print "Unacceptable ip address"

------------------------------------------------------------------------------------------------
if re.match("^[0-9 ]+$", myString):
    print "Only numbers and Spaces"


^[1-9][0-9]*$

https://stackoverflow.com/questions/11593022/regular-expressions-in-python-for-dissecting-ip
https://stackoverflow.com/questions/14132404/regex-accept-numeric-only-first-character-cant-be-0
https://stackoverflow.com/questions/4011855/regexp-to-check-if-an-ip-is-valid


def validate_and_split_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return None

    for part in parts:
        if not part.isdigit() or not 0<=int(part)<=255:
            return None
    return [int(part) for part in parts]
validate_and_split_ip('09.16.011.05')
--------------------------------------------------------------------
