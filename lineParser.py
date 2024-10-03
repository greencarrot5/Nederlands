import re

lineRegex = {

    "int_input": re.compile(r"^Vraag een getal$"),
    "int_init": re.compile(r"^Neem een getal, ([0-9]*)$"),
    "add": re.compile(r"^Tel er ([0-9]*) bij op$"),
    "subtract": re.compile(r"^Trek er ([0-9]*) van af$"),
    "print": re.compile(r"^Zeg (.*)$")

}

argRegex = {
    "string": re.compile(r"^\"([^\"]*)\"$"),
    "stack": re.compile(r"^het getal$")
}

def execLine(line, stack):

    intInitMatch = lineRegex["int_init"].match(line)

    if intInitMatch:
        #TODO: Controleer of het ding wel een int is
        stack.push(int(intInitMatch.group(1)))
        return None

    addMatch = lineRegex["add"].match(line)

    if addMatch:
        stack.push(stack.pop(True) + int(addMatch.group(1)))
        return None
    
    subtractMatch = lineRegex["subtract"].match(line)

    if subtractMatch:
        stack.push(stack.pop(True) - int(subtractMatch.group(1)))
        return None

    printMatch = lineRegex["print"].match(line)

    if printMatch:
        arg = printMatch.group(1)

        #Controleer wat het argument is
        strMatch = argRegex["string"].match(arg)

        if strMatch:
            print(strMatch.group(1))

            return None
        
        stackMatch = argRegex["stack"].match(arg)

        if stackMatch:
            print(stack.pop())

        return None
    
    intInputMatch = lineRegex["int_input"].match(line)

    if intInputMatch:
        stack.push(int(input("> ")))