#http://www.python-course.eu/recursive_functions.php
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
