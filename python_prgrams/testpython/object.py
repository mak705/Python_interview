movies = list()
movie1 = dict()
movie1['Director'] = 'James Cameroon'
movie1['Title'] = 'Avatar'
movie1['Relasing date'] = '18 Deember 2009'
movie1['Running Time'] = '144 minutes'
movie1['Rating'] = 'PG-13'
movies.append(movie1)
movie2 = dict()
movie2['Director'] = 'David Fincher'
movie2['Title'] = 'The Social Newtwork'
movie2['Relasing date'] = '01 October 2010'
movie2['Running Time'] = '140 minutes'
movie2['Rating'] = 'PG-11'
movies.append(movie2)
keys = ['Director','Title','Rating','Running Time']
print '-------------'
print movies
print '-------------'
print keys
for item in movies:
 print '-----------'
 for key in keys:
   print key,':',item[key]
print '----------'
