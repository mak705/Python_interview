letters = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"a","o":"a","p":"a","q":"a","r":"a","s":"a","t":"a","u":"a","v":"a","w":"a","x":"a","y":"a","z":"a"
}
message = raw_input("Enter the message")
encrypted = ""
for letter in message:
 if letter in letters:
  encrypted += letters[letter]
 else:
  encrypted += letter
print encrypted
