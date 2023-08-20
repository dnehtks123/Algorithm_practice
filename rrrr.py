left = list(input())
N = len(left)
right =[]
M = int(input())

for i in M:
    command = list(sys.stdin.readline().split())
    if command[0] == 'L' and left:
        left.pop()
    elif command[0] =='D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P' and left:
        left.append(command[1])
        
print(''.join(left + right[-1]))