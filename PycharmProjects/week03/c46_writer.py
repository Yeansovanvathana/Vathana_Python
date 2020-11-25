class Writer:
    @staticmethod
    def write(filename, text):
        writer = open(filename, 'w')
        writer.write(text+"\n")
        writer.close()
    @staticmethod
    def append(filename, text):
        writer = open(filename, 'a')
        writer.write(text+"\n")
writer = Writer()
print(writer.write("abc.txt", "hello!"))
print(writer.append("abc.txt", "bye!"))