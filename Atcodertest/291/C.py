def visited_twice(n, s):
    x, y = 0, 0
    visited = set([(0, 0)])

    for i in range(n):
        if s[i] == "R":
            x += 1
        elif s[i] == "L":
            x -= 1
        elif s[i] == "U":
            y += 1
        elif s[i] == "D":
            y -= 1

        pos = (x, y)
        if pos in visited:
            return "Yes"

        visited.add(pos)

    return "No"
n = int(input())
s = input()
print(visited_twice(n, s))