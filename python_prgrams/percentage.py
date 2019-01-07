if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        #print (name,scores)
        student_marks[line[0]] = list(map(float, line[1:]))
#print("{0:.2f}".format(sum(student_marks[line[0]])/(len(student_marks[line[0]]))))
#print (student_marks)
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
