#! /usr/bin/python3

import tempfile

OUT_FOLDER =""

user_d = dict(INPUT="myinfile", OUTPUT="myoutfile")

# This could be better as a dict of dict
para_d = dict(
    FASTQ = [("--i", "INPUT"), ("--o", "OUTPUT" ), ("--a", "OPTION")]
    )
prog_d = dict(
    FASTQ = "fastqc"
)

class Job():
    
    def __init__(self, name):
        self.name = name
        
    def buildCmdFile(self):

        cache_path = OUT_FOLDER + ".cache/"
        log_path = cache_path + self.name + "%j"
        tmp_path = cache_path + "tmp/"
        
        fd, cmd_path = tempfile.mkstemp(dir="tmp",prefix=self.name + "_")

        with open(cmd_path, "w") as tmp:
            tmp.write("""\
#!/bin/bash               
#@ job_name = {0}         
#@ initialdir = .         
#@ output = {1}.out       
#@ error = {1}.err        
#@ total_tasks = {2}      
#@ cpus_per_task = {3}    
#@ wall_clock_limit = {4} 
""".format()
)
        cmd = prog_d[self.name] + " "

        for i, j in para_d[self.name]:
            if j in user_d:
                cmd += i + " " + user_d[j] + " "

        return cmd

    def submit(self):
        cmd = self.buildCmdFile()
        print("mnsubmit " + cmd)


if __name__ == "__main__":

    myjob = Job("FASTQ")
    myjob.submit()
