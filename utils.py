
def fix_str(name):
    alias = {"Ckarl": "Carl", "Maxen": "Max", "Poggy": "Peggy", "Karl": "Carl", "Calle": "Carl", "Kalle": "Carl", "Epos": "Max"}
    name = name.replace(" ", "").capitalize()
    if name in alias:
        name = alias[name]
    return name

def vote_meaning(sign):
    if sign == "+":
        return "Up"
    if sign == "-":
        return "Down"
    return "Undefined"