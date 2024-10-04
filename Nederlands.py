import sys
import lineParser
from stackUtils import Stack
from programData import ProgramData

filename = sys.argv[1]
logfile = ""

if len(sys.argv) > 2:
    logfile = sys.argv[2]

with open(filename, "r") as f:
    #TODO: Zorg dat het puntkarakter in strings gebruikt kan worden.
    #Hoop voorlopig gewoon dat niemand dat doet.
    lines = f.read().split(".")

processed_lines = []

for line in lines:
    if "\n\n" in line:
        processed_lines.append("")

    line = line.replace("\n", "")

    if len(line) == 0:
        continue

    elif line[0] == " ":
        processed_lines.append(line[1:])

    else:
        processed_lines.append(line)

lines = processed_lines

stack = Stack()
data = ProgramData(lines, logfile)

while data.lineIndex < len(lines):
    currentLine = data.nextLine()

    lineIndex = lineParser.execLine(currentLine, data, stack)