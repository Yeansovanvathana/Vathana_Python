def dict_info(firstname, lastname, email, phone):
    return {"firstname": firstname.title(), "lastname": lastname.upper(), "email": email, "phone": phone}
dict_info("kevin", "sabbe", "sabb.kev@gmail.com", "+855 16 804 404")
dict_info("", "", "", "")