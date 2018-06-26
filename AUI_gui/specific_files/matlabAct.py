#ref https://www.programiz.com/python-programming/methods/built-in/exec

#ref https://www.mathworks.com/help/matlab/matlab-engine-for-python.html?requestedDomain=true
#ref https://www.mathworks.com/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html

#ref: http://www.pythonforbeginners.com/os/subprocess-for-system-administrators

x = 1
print(eval('x + 1'))

program = 'a = 5\nb=10\nprint "Sum = " + str(a+b)'
exec(program)

import subprocess

pathM = "C:/Program Files/MATLAB/R2015b/bin/"
pathMengine = "C:\Program Files\MATLAB\R2015b\extern\engines\python/"
pathMengine = u'C:\Program Files\MATLAB\R2015b\extern\engines\python/setup.py'
cmdStr = "python setup.py install"
# eval([pathMengine + cmdStr])
strCmd = "pyhton "+pathMengine + " install"
# eval(["pyhton "+pathMengine + " install"])
# eval(strCmd, globals=None, locals=None)
# exec strCmd
matScript = "matlabAction.m"
matlabroot = pathM + "ma tlab.exe"

try:
    print "activaeting.."
    subprocess.call(matlabroot)
except:
    print "cant do "+matlabroot

def run_win_cmd(cmd):
    result = []
    # process = subprocess.call(cmd,   #Popen(cmd,
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)

# run_win_cmd(matlabroot)

subprocess.check_output("dir C:", shell=True)