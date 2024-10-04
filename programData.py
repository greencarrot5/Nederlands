class ProgramData():
    def __init__(self, lines, logfile):
        self.lineIndex = 0

        self.lines = lines
        self.logfile = logfile

    def nextLine(self):
        self.lineIndex += 1
        return self.lines[self.lineIndex-1]
    
    def out(self, output):
        print(output)

        try:
            f = open(self.logfile, "r")
            fileExists = True
            f.close()
        except:
            fileExists = False

        if self.logfile != "":
            
            with open(self.logfile, "a") as f:
                if fileExists:
                    f.write("\n" + str(output))

                else:
                    f.write(str(output))