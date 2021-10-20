l = int(input())
arr = list(map(str, input().split()))
arr = "".join(arr)
print(arr)
def get_max_str(lst):
    return max(lst.split('0'), key=len)
print(len(get_max_str(arr)))