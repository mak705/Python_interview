
import re

def is_correct_regex(regex):
    try:
        re.compile(regex)
        return True
    except:
        return False

for _ in range(int(input())):
    print (is_correct_regex(input()))


Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex. 
.*+: Has the error multiple repeat. Hence, it is invalid.
