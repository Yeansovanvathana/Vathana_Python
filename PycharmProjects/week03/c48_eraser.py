import os
import random
class Eraser:
    @staticmethod
    def remove_file(filename):
        if os.path.exists("abc.txt"):
            os.remove("abc.txt")
        return random.choice(0, 1)
    @staticmethod
    def remove_folder(filename):
        if os.path.


print(Eraser().remove_folder("random_folder"))

