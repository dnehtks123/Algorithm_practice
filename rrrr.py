# 이코테 상하좌우 문제 풀이 따라써보기

n = int(input)
plans = sys.stdin.split.rstrip()
x, y = 1, 1


# 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types=[L, R, U, D]


# 이동계획을 하나씩 확인
for i in plans:
    # 이동 후 좌표 구하기
    for plan in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
#공간을 벗어나는 경우 무시
if nx < 1  or ny < 1 or nx > n or ny > n:
    continue
# 이동 수행

x, y = nx, ny




# 직접 생각하면서 따라서 작성 
n = int(input())
plans = int(input().split())

x,y=1,1

move_types=['L', 'R', 'U', 'U']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in plans:
    for plan in range(len(move_types)):
        if plan == move_types:
            nx = x + dx[i]
            ny = y + dy[i]

if nx > n or ny > n or nx < 1 or ny < 1 










# 1. 00 ~ 59 까지 횟수 세기 K
# 2. 초 : K * 60 번  + K + 0~N시에 있으면 + 1 ?

# 그냥 문자열로 바꿔서 푸네... 시계를 문자열로..ㅇㅎ


# 완전탐색
h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1