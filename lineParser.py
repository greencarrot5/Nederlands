import re
from argParser import parseArg

lineRegex = {

    "int_input": re.compile(r"^Vraag (nog )?een getal$"),
    "int_init": re.compile(r"^Neem (nog )?een getal, (.*)$"),
    "stack_swap": re.compile(r"^Neem het vorige getal$"),
    "add": re.compile(r"^Tel er (.*) bij op$"),
    "subtract": re.compile(r"^Trek er ([0-9]*) van af$"),
    "print": re.compile(r"^Zeg (.*)$"),
    "eternity": re.compile(r"^Blijf dat herhalen$"),
    "for": re.compile(r"^Doe dat (.*) keer$")

}

lastBreakpoint = 0

loops = {}

def execLine(line, data, stack):
    global lastBreakpoint

    if line == "":
        lastBreakpoint = data.lineIndex

    intInitMatch = lineRegex["int_init"].match(line)

    if intInitMatch:
        stack.push(parseArg(intInitMatch.group(2), stack))
    
    stackSwapMatch = lineRegex["stack_swap"].match(line)

    if stackSwapMatch:
        last = stack.pop(True)
        prev = stack.pop(True)

        stack.push(last)
        stack.push(prev)

    addMatch = lineRegex["add"].match(line)

    if addMatch:
        prevVal = stack.pop()
        addVal = parseArg(addMatch.group(1), stack)

        stack.pop(True)
        stack.push(prevVal + addVal)
    
    subtractMatch = lineRegex["subtract"].match(line)

    if subtractMatch:
        prevVal = stack.pop()
        subVal = parseArg(subtractMatch.group(1), stack)

        stack.pop(True)
        stack.push(prevVal - subVal)

    printMatch = lineRegex["print"].match(line)

    if printMatch:
        arg = printMatch.group(1)

        data.out(parseArg(arg, stack))
    
    intInputMatch = lineRegex["int_input"].match(line)

    if intInputMatch:
        stack.push(int(input("> ")))

    eternityMatch = lineRegex["eternity"].match(line)

    if eternityMatch:
        data.lineIndex = lastBreakpoint

    forMatch = lineRegex["for"].match(line)

    if forMatch:
        arg = parseArg(forMatch.group(1), stack)

        if data.lineIndex in loops.keys():
            if loops[data.lineIndex] > 0:
                loops[data.lineIndex] -= 1

                data.lineIndex = lastBreakpoint

        elif arg > 1:
            loops[data.lineIndex] = arg-2

            data.lineIndex = lastBreakpoint