n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
print (marksheet)

3
1
2
3
4
5
6
[['1', 2.0], ['3', 4.0], ['5', 6.0]]

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
marksheet

2
1
2
3
4

[['1', 2.0], ['3', 4.0]]

a = [['a', 1.0], ['b', 2.0],['c', 3.0], ['d', 4.0]]
second_highest = sorted(list(set([marks for name, marks in a])))[-2]
print('\n'.join([a for a,b in sorted(a) if b == second_highest]))

c

second_highest
3.0 
