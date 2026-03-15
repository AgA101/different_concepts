n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
        a[i] = list(map(int, input().split()))
k = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = 0
            a[j][i] = 0
            k += 1
print(k)

            
