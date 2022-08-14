if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name = line[0]
        scores = line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for key in student_marks:
        if key == query_name:
            for score in student_marks[key]:
                sum = sum + score
    avg = sum/3
    print("{0:.2f}".format(avg)) 
