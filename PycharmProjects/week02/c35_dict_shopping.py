def dict_shopping(l):
    total_price = 0
    quantity = 0
    if len(l) < 1:
        return ('Invalid JSON', 0)
    for i in l:
        if "price" in i and "quantity" in i:
            if i["price"] >= 0.01 and i["quantity"] >= 1:
                total = i["price"] * i["quantity"]
                total_price += total
                quantity += i["quantity"]
            else:
                return ('Invalid JSON', 0)
    total_price = round(total_price, 2)
    return ('$' + str(total_price), quantity)
# dict_shopping([{"price" : 19.99, "quantity": 3},
#                {"price" : 99.99,"quantity" : 6}])