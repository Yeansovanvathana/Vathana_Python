class StringFormat:
    @staticmethod
    def first(first):
        return first[:1]
    @staticmethod
    def last(last):
        return last[-1]
    @staticmethod
    def lower(low):
        return low.lower()
    @staticmethod
    def upper(up):
        return up.upper()
    @staticmethod
    def reversed(reverse):
        return reverse[::-1]

str_format = StringFormat()
print(str_format.first("Python"))
print(str_format.last("Python"))
print(str_format.lower("Python"))
print(str_format.upper("Python"))
print(str_format.reversed("Python"))
