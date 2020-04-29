"""
Simple matching in python implmement in
two aways

"""
def match(i):
    if i == 42:
        return "The Answer"
    elif i == 43:
        return "Close but not quite"
    else:
        return "I can't match that!"

def match2(i):
    return (
        "The Answer" if i == 42 else
        "Close but not quite" if i == 43 else
        "I can't match that!"
    )

print(match(42))
print(match2(43))
