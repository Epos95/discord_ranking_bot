
def fix_str(name):
    name = name.replace(" ", "").capitalize()
    return name

def vote_meaning(sign):
    if sign == "+":
        return "Up"
    if sign == "-":
        return "Down"
    return "Undefined"

# This function will return what type of vote, voter, votie, reason.
# arg should be the whole message, not just the content.
def get_vote(message):
    content = message.content
    author = message.author.id
    name = ""
    reason = ""
    is_reason = False
    character_not_name = [' ', '+', '-']
    # This for-loop will take out name and reason in variables form content (message.content)
    for i in content:
        if i == '(' or is_reason:
            if i != '(' and i != ')':
                reason += i
            is_reason = True
        elif i not in character_not_name:
            name += i
    
    vote_info = {"author_id": str(author), "name": str(name), "reason": str(reason)}
    return vote_info