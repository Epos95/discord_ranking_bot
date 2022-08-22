import re


#from memory import Stats

def fix_str(name):
    if type(name) != str:
        raise TypeError(
            f"Wrong type in utilfunction fix_str, got {type(name)} when expecting str"
        )

    name = name.replace(" ", "").capitalize()
    return name


def vote_meaning(sign):
    if type(sign) != str:
        raise TypeError(
            f"Wrong type in utilfunction vote_meaning, got {type(sign)} when expecting str"
        )

    if sign == "+":
        return "Up"
    if sign == "-":
        return "Down"
    return "Undefined"


# This function will return what type of vote, voter, votie, reason.
# arg should be the whole message, not just the content.
def get_vote(message, memoryHandle):
    content = message.content
    author = message.author.id
    name = ""
    reason = ""
    is_reason = False
    character_not_name = [" ", "+", "-"]
    # This for-loop will take out name and reason in variables form content (message.content)

    tagVoteName = re.search("<@([0-9]{18})>", content)
    if tagVoteName:
        name = memoryHandle.id_name(tagVoteName.group(1))
    for i in content:
        if i == "(" or is_reason:
            if i != "(" and i != ")":
                reason += i
            is_reason = True
        elif (i not in character_not_name) and not tagVoteName:
            name += i

    vote_info = {"author_id": str(author), "name": str(name), "reason": str(reason)}
    return vote_info
