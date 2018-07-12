from sys import argv
script, from_file, to_file = argv
txt = open(from_file)
data =  txt.read()
out_file = open(to_file,'w')
out_file.write(data)

txt.close()
out_file.close()
 
