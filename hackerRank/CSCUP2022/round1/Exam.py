n, m, f, i = map(int, input().split())

Student = n - i
PassBoth = m + f - Student
PassMath = m - PassBoth
PassPhysic = f - PassBoth

print(PassBoth, PassMath, PassPhysic)

