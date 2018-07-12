def outer_function(): #outer function doesnt take any params
    message = 'Hi'  # Locat variable
    def inner_function(): #Inner function will print the result
        print message
    return inner_function()
outer_function()

>> Hi
-------------------------------------------------------------------
def outer_function(): #outer function doesnt take any params
    message = 'Hi'  # Locat variable
    def inner_function(): #Inner function will print the result
        print message
    return inner_function
my_func = outer_function()
my_func()

>> Hi
-------------------------------------------------------------------
#DECORATOER
#decorator > taking other function as argument
def decorator_function(orginal_function):
    def wrapper_function(): #Inner function will print the result
        return orginal_function()
    return wrapper_function
def display():
    print 'display function ran'
decorated_dispaly = decorator_function(display) #dispaly function = orginal function with no decorator and return 
#the orginal function in this case its dislay function
#decorator function waiting wrapper function to be executed will
#return the orginal function
decorated_dispaly() #actuallly executing  wrapper function  which then execting display function and print
#display function ran 

>> display function ran

---------------------------------------------------------------------

#decorator will help to add functionality to our existing functions, by adding functionallty inside the wrapper
def decorator_function(orginal_function):
    def wrapper_function(): 
        print ('wrapper executed this before {}'.format(orginal_function.__name__))#We can see this message
#print first before the orginal function
        return orginal_function()
    return wrapper_function
def display():
    print 'display function ran'
decorated_dispaly = decorator_function(display)
decorated_dispaly()

>>wrapper executed this before display
display function ran
---------------------------------------------------------------------
#decorator will help to add functionality to our existing functions, by adding functionallty inside the wrapper
def decorator_function(orginal_function):
    def wrapper_function(): 
        print ('wrapper executed this before {}'.format(orginal_function.__name__))#We can see this message
#print first before the orginal function
        return orginal_function()
    return wrapper_function
@decorator_function
def display():
    print 'display function ran'
decorated_dispaly = decorator_function(display)
display()

#@decorator_function => display = decorator_function(display) 
#decorated_dispaly()

>> wrapper executed this before display
display function ran

------------------------------------------------------------------------
def decorator_function(orginal_function):
    def wrapper_function(): 
        print ('wrapper executed this before {}'.format(orginal_function.__name__))#We can see this message
#print first before the orginal function
        return orginal_function()
    return wrapper_function
@decorator_function
def display():
    print 'display function ran'
decorated_dispaly = decorator_function(display)
def display_info(name,age):
    print ('display info ran with the args({},{})'.format(name,age))
display_info('mak',28)
display()

>> display info ran with the args(mak,28)
wrapper executed this before display
display function ran
---------------------------------------------------------------------------
def decorator_function(orginal_function):
    def wrapper_function(*args,**kwargs): 
        print ('wrapper executed this before {}'.format(orginal_function.__name__))#We can see this message
#print first before the orginal function
        return orginal_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def display():
    print 'display function ran'
decorated_dispaly = decorator_function(display)
@decorator_function
def display_info(name,age):
    print ('display info ran with the args({},{})'.format(name,age))
display_info('mak',28)  # if we dont give *args and **kwargs it will throw error as argument 2 given 
display()

>>wrapper executed this before display_info
display info ran with the args(mak,28)
wrapper executed this before display
display function ran

-------------------------------------------------------------------------
def decorator_function(orginal_function):
    def wrapper_function(*args,**kwargs): 
        print ('wrapper executed this before {}'.format(orginal_function.__name__))#We can see this message
#print first before the orginal function
        return orginal_function(*args,**kwargs)
    return wrapper_function

class decorator_class(object):
    def __init__(self,orginal_function):
        self.orginal_function = orginal_function
    def __call__(self, *args,**kwargs):
        print ('Call executed this before {}'.format(self.orginal_function.__name__))
        return self.orginal_function(*args,**kwargs)

@decorator_class
def display():
    print 'display function ran'
decorated_dispaly = decorator_function(display)
@decorator_class
def display_info(name,age):
    print ('display info ran with the args({},{})'.format(name,age))
display_info('mak',28)
display()

>>Call executed this before display_info
display info ran with the args(mak,28)
Call executed this before display
display function ran
------------------------------------------------------------------------
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Rans with args:{}, and kwargs {}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
@my_logger
def display_info(name,age):
    print 'display info ran with 2 argument ({},{})'.format(name,age)
display_info('mak',28)
#run as python file , you will login report as display_info.log

>> display info ran with 2 argument (mak,28)
---------------------------------------------------------------------------
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, kwargs:{}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
@my_logger
def display_info(name,age):
    print 'display info ran with 2 argument ({},{})'.format(name,age)
display_info('mak', 28)

>> display info ran with 2 argument (mak,28)
---------------------------------------------------------------------------
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, kwargs:{}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() -t1
        print ('{} ran in : {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper
import time
    
@my_timer
def display_info(name,age):
    time.sleep(1)
    print 'display info ran with 2 argument ({},{})'.format(name,age)
display_info('mak', 28)


>>display info ran with 2 argument (mak,28)
display_info ran in : 1.00041294098 sec

-------------------------------------------------------------------

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, kwargs:{}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() -t1
        print ('{} ran in : {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper
import time
    
@my_timer
@my_logger
def display_info(name,age):
    time.sleep(1)
    print 'display info ran with 2 argument ({},{})'.format(name,age)
display_info('mak', 28) #Some random output which we dont want, we want display in ran 1.0 sec in the 
#log file output wont added

>> display info ran with 2 argument (mak,28)
wrapper ran in : 1.00123000145 sec

------------------------------------------------------------------------

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, kwargs:{}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() -t1
        print ('{} ran in : {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper
import time

#@my_logger
#@my_timer
def display_info(name,age):
    time.sleep(1)
    print 'display info ran with 2 argument ({},{})'.format(name,age)
display_info = my_timer(display_info)

print (display_info.__name__)

display_info('mak',28)

>>wrapper
display info ran with 2 argument (mak,28)
display_info ran in : 1.00207591057 sec
------------------------------------------------------------------------

from functools import wraps 
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, kwargs:{}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() -t1
        print ('{} ran in : {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper
import time

#@my_logger
#@my_timer
def display_info(name,age):
    time.sleep(1)
    print 'display info ran with 2 argument ({},{})'.format(name,age)
display_info = my_timer(display_info)

print (display_info.__name__)

display_info('mak',28)

>> display_info
display info ran with 2 argument (mak,28)
display_info ran in : 1.00178098679 sec















