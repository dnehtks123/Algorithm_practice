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


# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================

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
                
# 왕실의 나이트
start = input()
x = int(start[1])
y_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = y_list.index(start[0])+1

# 상좌(-2, -1), 상우(-2, 1), 우상(2, -1), 우하(2, 1), 좌상(-2, -1), 좌하(-2, 1), 하좌(2, -1), 하우(2, 1)
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-2, -1), (-2, 1), (2, -1), (2, 1)]

count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if (nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
        count += 1  

print(count)

# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================


# 삼성전자 알고리즘 테스트 문제. 

# n,m을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 생성해서 0으로 초기화
d = [[0]*M for _ in range(N)]

# 현재 캐릭터의 x, y 좌표 받기
a, b, direction = map(int, input().split())
d[x][y] = 1 # 자기 자리 1처리

# 전체 맵 정보를 입력받기
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
# 왼쪽으로 회전
def turn_left():
    global_direction 
    direction -=1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time =  0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count+=1
        turn_time = 0
        continue
    #  회전한 이후 갈 곳이 없다면 회전만 하기
    else:
        turn_time+=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time ==4:
        nx = x + dx[direction]    
        ny = y + dy[direction] 
        #뒤가 바다로 막혀있는경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time=0
        
# 정답 출력
print(count)

# 다시한번 복습
# N, M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

a, b, direction = map(int, input().split())

array=[]
for _ in range(n):
    array.append(list(map(int, input().split())))

# 리스트 컴프리헨션으로 모두 0으로 처리
d = [[0] * m for _ in range(n)]
# 1. 왼쪽 방향 부터 갈 곳을 정한다
def turn_left:
    global direction
    direction -=1
    if direction==-1:
        direction=3
        
# 2. 가보지 않은 칸 0이 있다면 전진
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        turn_time = 0
        count+=1
        continue
# 3. 가봤던 칸 else 이라면 회전만 하기
    else:        
        turn_time+=1
# 4. 네 방향 모두 가본 칸 turn_time == 4
    if turn_time == 4:
        # 뒤로갈수있음이동
        nx = x - dx[direction]
        ny = y - dx[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time=0
print(count)

# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================


# DFS, BFS 알고리즘 재귀함수로 구현

# 1. DFS   ----> 스택 동작원리, 구현 법 재귀함수
def dfs(graph, v, visited):
    # 현재 노드를 방문처리 후 print로 확인
    visited[v] =True
        print(v, end=' ')
        
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
     
# 2. BFS  ========> 큐 동작원리
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 1. 음료수 얼려먹기
n, m = map(int, input().split())

def dfs(x, y):
    if x <= -1 or x >=n or y<= -1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해서 음료수 채우기
result = 0
for i in range(n):
    fot j in range(m):
        if dfs(i,j) == True:
            result+=1
            
print(result)
        
            
visited = ['False'] * n

# 얼음 틀 전달받기 dfs?, bfs? 구현?

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dfs(x-1, y) # 좌
dfs(x+1, y) # 우
dfs(x, y-1) # 상
dfs(x, y+1) # 하




# 2. 미로탈출

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0] 
dy = [0, 0,-1, 1]

def bfs(x, y):
    queue=deque()    
    queue.append((x,y))
    
    while queue: # 큐가 빌때까지 반복
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or ny <0 or nx >n or ny >m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하면 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    
    