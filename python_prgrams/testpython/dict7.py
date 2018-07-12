name = raw_input("Enter a file name")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name,'r')
text = handle.read()
print len(text),text[:40]
words = text.split()
print len(words)
counts = dict()
for word in words:
 counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
 if bigcount is None or count > bigcount:
  bigword = word
  bigcount = count
print bigword,bigcount
