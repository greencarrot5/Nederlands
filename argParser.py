import re

argRegex = {
    "int": re.compile(r"^([0-9]*)$"),
    "string": re.compile(r"^\"([^\"]*)\"$"),
    "stack": re.compile(r"^het getal$"),
    "stack_2": re.compile(r"^het vorige getal$")
}

def parseArg(arg, stack):
    #Controleer wat het argument is
    intMatch = argRegex["int"].match(arg)

    if intMatch:
        return int(intMatch.group(1))

    strMatch = argRegex["string"].match(arg)

    if strMatch:
        return strMatch.group(1)
        
    stackMatch = argRegex["stack"].match(arg)

    if stackMatch:
        return stack.pop()
    
    stack2Match = argRegex["stack_2"].match(arg)

    if stack2Match:
        last = stack.pop(True)
        previous = stack.pop()
        stack.push(last)

        return previous