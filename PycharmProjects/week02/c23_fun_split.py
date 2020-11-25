def fun_split(lis):
    if lis:
        word = lis.split()
    elif lis == "":
        return []
    return word
fun_split("")
fun_split("Hello")
fun_split("Hello World!")
fun_split("one two three four five")

