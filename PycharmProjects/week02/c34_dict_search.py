def dict_search(info_students, search):
    if search in info_students:
        return info_students[search]
    else:
        return "ERROR: '"+search+"' key not found."
info_student = {"username": "sabb_k", "score": 100, "comments": "Good job!"}
(dict_search(info_student, "comments"))