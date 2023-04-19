N = int(input())
A = list(map(int, input().split()))
people = list(range(1, N+1))
people1 = list(range(1, N+1))
called = []
num = []
for i in range(N):
    if A[i] in people:
        print("people", people)
        print("called", called)
        print("person call other", num)
        print("Id : ", people1[i])
        if people1[i] not in called:
            print(i + 1, A[i], people)
            people.remove(A[i])
            called.append(A[i])
            num.append(i + 1)
# print(*sorted(people))
print(called)
