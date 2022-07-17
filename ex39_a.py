def pr_dict(dict):
    for key, value in list(dict.items()):
        print(key, value)

def pr_dash():
    print("-" * 10)


capitols = {
    "China": "Beijing",
    "Japan": "Tokyo",
    "South Korea": "Seoul",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "India": "New Delhi",
}

foods = {
    "Hot Dogs": "Chicago",
    "Spaghetti": "Kuala Lumpur",
    "Bangers and Mash": "Kyrgyzstan",
    "Weinerschnitzel": "Georgia.  The state, not the country.",
    "Goodbye": "English",
    "Off Vederzain": "Also English",
    "Ohio Gozimus": "You guessed it.  English"
}

capCopy = capitols.copy()
capDupe = capitols

# del capitols["China"]
# pr_dict(capCopy)
# pr_dash()
# pr_dict(capitols)
# pr_dash()
# pr_dict(capDupe)
# pr_dash()
# v = capitols.pop("Iraq")
# print(v)
# key, value = capitols.popitem()
# print(key, value)

v = capitols.setdefault("Bop", "Doot")


# for k,v in capitols.items():
#     print(k,v)

capitols.update(capCopy)

pr_dict(capitols)