original_dict = {'jack': {'age':35, 'status': 'single'}, 
'stephan': {'age':27, 'status': 'married'},
'anna': {'age':29, 'status': 'married'},
'max': {'age':37, 'status': 'single'}}

# Transform the dict into a list of dicts
people = [{k: v} for k, v in original_dict.items()]
# Unpack the first 4 elements of the list into 4 new variables
a, b, c, e = people[:4]

a
>{'jack': {'age': 35, 'status': 'single'}}
