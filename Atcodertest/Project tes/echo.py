n = int(input())
S = input()
firstpart, secondpart = S[:int(len(S)/2)], S[int(len(S)/2):]
print("Yes") if firstpart == secondpart else print("No")

