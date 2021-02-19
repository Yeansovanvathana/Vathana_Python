# n,m = map(int,input().split())
# ab = [list(map(int,input().split())) for x in [0]*n]
# cd = [list(map(int,input().split())) for x in [0]*m]
# print(ab)
# print(cd)
# for a,b in ab:
#     # for c,d in cd:
#     #     print(c)
#     l = [abs(a-c)+abs(b-d) for c,d in cd]
#     # print(l.index(min(l))+1)
#     print(l.index(min(l)))

# firstpart, secondpart = S[:int(len(S)/2)], S[int(len(S)/2):]

# print("Yes") if firstpart == secondpart else print("No")

import math
# sys.setrecursionlimit(10 ** 8)

def mod(n):
    return n % (10 ** 9 + 7)

def sinput():
    return sys.stdin.readline()[:-1]

def prime(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def div(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def GCD(n, m):
    return math.gcd(n, m)
def LCM(n, m):
    return n * m / GCD(n, m)
# def lcm(x, y):
#     return (x * y) // math.gcd(x, y)

def C(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def P(n, r):
    if n < r:
        return 0
    return math.factorial(n) // math.factorial(n - r)

def cos(x, y, a):
    return (x ** 2 + y ** 2 - 2 * x * y * math.cos(math.radians(a))) ** 0.5

def inp():  # n=1
    return int(input())


def inpm():  # x=1,y=2
    return map(int, input().split())


def inpl():  # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))


def inpls():  # a=['1','2','3',...,'n']
    return list(input().split())


def inplm(n):  # x=[] 複数行
    return list(int(input()) for _ in range(n))


def inpll(n):  # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])


def sortx(x, n, k):
    if k == 0:
        x.sort(key=lambda y: y[1, n])
    else:
        x.sort(reversed=True, key=lambda y: y[1, n])


def graph():
    n = inp()
    g = [[] for _ in range(n)]
    for i in range(n):
        a = inp()
        a -= 1
        g[i].append(a)
        g[a].append(i)
    return n, g


def graphm():
    n, m = inpm()
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = inpm()
        a -= 1
        b -= 1
        g[a].append((b, w))
        g[b].append((a, w))
    return n, m, g
def BFS(g, q, pos=None):
    if pos is None:
        pos = set()
    if type(q) == deque:
        pos.add(q)
        q = deque([q])
    pos.add(q[-1])
    for i in g[q.pop()]:
        if not i in pos:
            q.append(i)
    while q != deque():
        pos, q = BFS(g, q, pos)
    return pos, q


def DFS_one(g, s, pos=None):
    if pos is None:
        pos = set()
    pos = copy(pos)
    pos.add(s)
    b = copy(pos)
    m = copy(pos)
    for i in g[s]:
        if not (i in pos):
            b = DFS(g, i, pos)
            if len(m) < len(b):
                m = b
    return m


def main():
    r=inp()
    print(r**2)
if __name__ == "__main__":
    main()