n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
average = sum(marks) / len(marks)
print('{0:.2f}'.format(average))