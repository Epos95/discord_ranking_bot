
def fix_str(name):
    name = name.replace(" ", "").capitalize()
    return name

def vote_meaning(sign):
    if sign == "+":
        return "Up"
    if sign == "-":
        return "Down"
    return "Undefined"