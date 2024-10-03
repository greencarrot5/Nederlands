import sys
import lineParser
from stackUtils import Stack

filename = sys.argv[1]

with open(filename, "r") as f:
    #TODO: Zorg dat het puntkarakter in strings gebruikt kan worden.
    #Hoop voorlopig gewoon dat niemand dat doet.
    lines = f.read().replace("\n", "").split(".")

processed_lines = []

for line in lines:
    if len(line) == 0:
        continue

    if line[0] == " ":
        processed_lines.append(line[1:])

    else:
        processed_lines.append(line)

lines = processed_lines

stack = Stack()

lineIndex = 0

while lineIndex < len(lines):
    currentLine = lines[lineIndex]

    lineParser.execLine(currentLine, stack)

    lineIndex += 1