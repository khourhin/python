import random
request =["cmd1", "cmd2", "cmd3"]
prelimCmds = {"cmd1": ["cmd1.1", "cmd1.2"], "cmd3":["cmd3.1"]}
deps = { "cmd1": [], "cmd2": ["cmd1"], "cmd3":["cmd1", "cmd2"] }

class JobManager():
    def __init__(self, request):
        self.request = request

    def launch(self):
        for progName in self.request:
            cs = CommandSubmiter(progName)
            cs.getPrelimCommands()            
            cs.submitAll()
        cs.resetDep()

class CommandSubmiter():
    depDict = {'dep':[]}
    
    def __init__(self, progName):
        self.progName = progName
        self.commands = []

    def getPrelimCommands(self):
        if self.progName in prelimCmds:
            for prelimCmd in prelimCmds[self.progName]:
                self.commands.append(Command(prelimCmd))

        self.commands.append(Command(self.progName))

        return self.commands
        
    def submitAll(self):
        for command in self.commands:
            command.createCmdFile()
            slurmid = command.submit( self.depDict )
            self.depDict['dep'].append(slurmid)

    def resetDep(self):
        self.depDict = {'dep':[]}

class Command():

    def __init__(self, cmd):
        self.cmd = cmd
        self.cmdFile = cmd + ".txt"

    def createCmdFile(self):
        with open(self.cmdFile, "wb") as cmdF:
            cmdF.write("Starting in file %s" % (self.cmd, ))

    def formatDeps(self):
        pass
    
    def submit(self, depDict):
        slurmid = random.randint(0,100)
        print self.cmd, "slurmid:%d " % (slurmid,)
        print depDict
        return slurmid
                
if __name__ == "__main__":
    job = JobManager(request)
    job.launch()
    job.launch()
                    
