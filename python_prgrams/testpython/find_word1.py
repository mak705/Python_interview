def find_word(search_term, word_list):
    matching_words = []
    for element in word_list:
        if search_term in element:
            matching_words.append(element)
    return matching_words
mystrings = [ 'frog', 'fox', 'foxtrot', 'toad' ]
words_found = find_word('toad', mystrings)
print "I found:", words_found, "my search term was:", 'fox' 
