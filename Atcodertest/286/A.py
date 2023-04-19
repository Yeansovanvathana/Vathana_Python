n = int(input())
S = input()
i = 0
result = ""
while i < len(S) - 1:
    if S[i] == "n" and S[i+1] == "a":
        result += "nya"
        i += 2
    else:
        result += S[i]
        i += 1
if i < len(S):
    result += S[i]
print(result)