def validator(string):
    stack = []
    Dict = {"(" : ")", "{" : "}", "[" : "]"}
    for i in string:
        if i in "({[":
            stack.append(i)
        elif i in "}])" and Dict[stack[-1]] == i and len(stack) != 0:
            stack.pop()
        elif len(stack) == 0 and i == "}])":
            return False
    if len(stack) == 0:
        return True
    else:
        return False

string = "(){(}[]"
print (validator(string))