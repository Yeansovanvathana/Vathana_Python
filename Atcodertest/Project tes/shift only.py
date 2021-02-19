n = int(input())
lis = list(map(int, input().split()))
count = 0
while True:
    for item in lis:
        if item % 2 != 0:
            print(count)
            exit()
    count += 1
    lis = [x/2 for x in lis]
