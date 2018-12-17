import subprocess, commands, os

#subprocess
p = subprocess.Popen(['ls', '-lia'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out

#subprocess
output = subprocess.Popen(['ls', '-lia'], stdout=subprocess.PIPE).communicate()[0]

#commands: The function getstatusoutput() runs a command via the shell and returns the exit code and the text output (stdout and stderr combined)
#Deprecated since version 2.6
status, text = commands.getstatusoutput('ls -lia')
print text

#subprocess yield
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break
#Note, that I'm redirecting stderr to stdout, it might not be exactly what you want, but I want error messages also.
#This function yields line by line as they come (normally you'd have to wait for subprocess to finish to get the output as a whole).
#For your case the usage would be:

for line in runProcess('ls -lia'.split()):
    print line,

#os.system
os.system('ls -lia')
