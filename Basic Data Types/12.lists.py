if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(1,N+1):
        command = input().split()
        if command[0] == "insert":
            index = int(command[1])
            num = int(command[2])
            list.insert(index, num)
        elif command[0] == "remove":
            num = int(command[1])
            list.remove(num)
        elif command[0] == "append":
            num = int(command[1])
            list.append(num)
        elif command[0] == "sort":
            list.sort()
        elif command[0] == "pop":
            list.pop()
        elif command[0] == "reverse":
            list.reverse()
        elif command[0] == "print":
            print(list)