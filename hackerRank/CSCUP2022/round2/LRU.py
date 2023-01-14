from collections import deque

def get(dic, order, key):
    if key not in dic:
        return -1
    value = dic[key]
    order.remove(key)
    order.append(key)
    return value

def set(dic, key, value):
    if key in dic:
        order.remove(key)
    elif key not in dic and len(dic) == size:
        tmp = order.popleft()
        dic.pop(tmp)
    order.append(key)
    dic[key] = value


optType_count = int(input().strip())

optType = []

for _ in range(optType_count):
    optType_item = input()
    optType.append(optType_item)

optValue_count = int(input().strip())

optValue = []

for _ in range(optValue_count):
    optValue_item = input()
    L = optValue_item.find(',')
    if L > 0:
        optValue.append(optValue_item.split(",", 1))
    else:
        optValue.append(optValue_item)

size = optValue[0]
capacity = size
dic = {}
order = deque()

optType.pop(0)
optValue.pop(0)

ans = []
for i in range(len(optType)):
    if optType[i] == 'put':
        K2 = set(dic, optValue[i][0], optValue[i][0])
        # ans.append(K2)


    else:
        K3 = get(dic, order, optValue[i])
        # ans.append(K3)

print(dic)
print(order)
# ans = [i for i in ans if i]
#
# final = []
# num = -1
# print(ans)
# for j in range(int(capacity)):
#     final.append(ans[num])
#     num -= 1

# print(",".join(final))

