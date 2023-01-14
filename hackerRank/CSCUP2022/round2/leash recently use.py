def get(dic, key):
    if key not in dic:
        return -1
    dic[key] = dic.pop(key)
    return dic[key]


def put(dic, capacity, key, value):
    # dic.pop(key)
    dic[key] = value
    if len(dic) > capacity:
        dic.pop(next(iter(dic.keys()), None))


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
dic = []
# order = deque()

optType.pop(0)
optValue.pop(0)
# print(optType, optValue)
ans = []
for i in range(len(optType)):
    if optType[i] == 'put':
        K2 = put(dic, capacity, optValue[i][0], optValue[i][0])
        ans.append(K2)
        # print('k', K2)

    else:
        K3 = get(dic, optValue[i])
        ans.append(K3)
        # print(K3)
# print(ans[:5])
# ans.remove(None)
ans = [i for i in ans if i]
print(ans)

# ans1 = ans[-1]
# ans2 = ans[-2]
# # final = []
# # final.append(ans2)
# # final.append(ans1)
#
# print(f'{ans1},{ans2}')
