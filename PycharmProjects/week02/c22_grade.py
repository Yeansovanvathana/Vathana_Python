def grade(int):
    if (int >= 90) and (int <= 100):
        return ("A")
    elif (int >= 80) and (int <= 89):
        return ("B")
    elif (int >= 70) and (int <= 79):
        return ("C")
    elif (int >= 60) and (int <= 69):
        return ("D")
    elif (int <= 59):
        return ("F")
    return "F"
grade(100)