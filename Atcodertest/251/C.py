n = int(input())
s = []
t = []
for i in range(n):
    S, T = map(str,input().split())
    s.append(S)
    t.append(int(T))
dic = {}
for i in range(len(s)):
    if s[i] not in dic.keys():
        dic[s[i]] = t[i]
max_key = max(dic, key=dic.get)
print(s.index(max_key) + 1)