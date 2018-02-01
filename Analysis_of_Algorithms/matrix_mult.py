from __future__ import print_function

def print_optimal(s,i,j):
    if(i==j):
        print("A",i,end='')
    else:
        print("(",end='')
        print_optimal(s,i,s[i][j])
        print_optimal(s,s[i][j]+1,j)
        print(")",end='')


p = [5,10,3,12,5,50,6]
#print len(p)
n = len(p) - 1

m = [[0 for x in range(n+1)] for y in range(n+1)]
s = [[0 for x in range(n+1)] for y in range(n)]

for l in range(2,n+1):
    for i in range(1,n-l+2):
        j = i+l-1
        m[i][j] = 9999999
        for k in range(i,j):
            q = m[i][k] + m[k+1][j] + (p[i-1]*p[k]*p[j])
            if(q < m[i][j]):
                m[i][j] = q
                s[i][j] = k

print(m)
print(s)
print_optimal(s,1,6)
