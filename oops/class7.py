#Decoraters
#passing arguments as function
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()

------------------------------------

#Decoraters
#passing arguments as function
def decorator_function(original_function):
    def wrapper_function():
        print ('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()

------------------------------------------------

#Decoraters
#passing arguments as function
def decorator_function(original_function):
    def wrapper_function():
        print ('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print('display function ran')

------------------------------------------------
#Decoraters
#passing arguments as function
def decorator_function(original_function):
    def wrapper_function():
        print ('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print('display function ran')
#display = decorator_function(display)  == @decorator_function
    
display()

-------------------------------------------------


#Decoraters
#passing arguments as function
def decorator_function(original_function):
    def wrapper_function():
        print ('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print('display function ran')
#display = decorator_function(display)  == @decorator_function

def display_info(name,age):
    print ('display_info ran with arguments({},{})').format(name,age)
    
display_info('Mak', 28)   
#display()

---------------------------------------------------------------





