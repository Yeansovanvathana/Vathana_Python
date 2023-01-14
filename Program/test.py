def FindActualX(equation):
    left, right = equation.split("=")
    if "+" in left:
        first, second = left.split("+")
        print(first, second)
        if "x" in first:
            ans = int(right) - int(second)
            final_ans = str(first).index("x")
            print(f"final {final_ans}")
            print(str(ans)[final_ans])
        if "x" in second:
            ans = int(right) - int(first)
            final_ans = str(second).index("x")
            print(str(ans)[final_ans])
    if "-" in left:
        first, second = left.split("-")
        if "x" in first:
            ans = int(right) + int(second)
            final_ans = str(first).index("x")
            print(str(ans)[final_ans])
        if "x" in second:
            ans = -(int(right) - int(first))
            final_ans = str(second).index("x")
            print(final_ans)
            print(str(ans)[final_ans])
    if "*" in left:
        first, second = left.split("*")
        if "x" in first:
            ans = int(right) / int(second)
            final_ans = str(first).index("x")
            print(str(ans)[final_ans])
        if "x" in second:
            ans = int(right) / int(first)
            final_ans = str(second).index("x")
            print(str(ans)[final_ans])
    if "/" in left:
        first, second = left.split("/")
        if "x" in first:
            ans = int(right) * int(second)
            final_ans = str(first).index("x")
            print(str(ans)[final_ans])
        if "x" in second:
            ans = int(right) * int(first)
            final_ans = str(second).index("x")
            print(str(ans)[final_ans])
    if "x" in right:
        if "-" in left:
            first, second = left.split("-")
            ans = int(first) - int(second)
            final_ans = str(right).index("x")
            print(str(ans)[final_ans])

FindActualX("3x+5=35")
FindActualX("20-x=15")
FindActualX("12*1x=120")
FindActualX("15-5=x0")
FindActualX("1x/3=4")

