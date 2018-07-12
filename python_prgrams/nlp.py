import string
from nltk.corpus import stopwords
stopwords.words('english')[0:10]
test_string = "This is my first test! wow! we are doing fine"
no_punctuations = [char for char in test_string if char not in string.punctuation]
no_punctuations
no_punctuations = ''.join(no_punctuations)
no_punctuations


