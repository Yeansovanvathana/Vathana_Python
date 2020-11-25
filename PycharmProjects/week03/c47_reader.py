class Reader:

    @staticmethod
    def read(filename):
        read = open(filename, 'r')
        return read.read().rstrip()
    @staticmethod
    def readline(filename):
        read = open(filename, 'r')
        return read.read().rstrip().split()

reader = Reader()
print(reader.read("abc.txt"))
print(reader.readline("abc.txt"))