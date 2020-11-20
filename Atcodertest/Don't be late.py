def main():
    D, T, S = map(int, input().split())
    speed = D / T
    if speed <= S:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
d, t, s = map(int, input().split())

if (t * s >= d):
    print("Yes")
else:
    print("No")

D, T, S = map(int, input().split())
if (T * S >= D):
    print("Yes")
else:
    print("No")
