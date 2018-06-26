# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 14:22:44 2018

matlab activation
from 
https://www.mathworks.com/help/matlab/matlab_external/start-the-matlab-engine-for-python.html
https://www.mathworks.com/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html

installation of the matlab engine package:
   by https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
   i.e :
       open command shell from windows shortcut as administrator console.
       change dir to : cd "matlabroot\extern\engines\python"
       then run : python setup.py install
       it will compile the code (or set proper copy of the 'dist' path),
         and the python instalation (i.e spyder) will get familiar from now on 
         with the 'import matlab' package.
"""
# Start MATLAB Engine for Python
import matlab.engine

# Run Multiple Engines
eng1 = matlab.engine.start_matlab()
eng2 = matlab.engine.start_matlab()

eng1.desktop(nargout=0)

# Stop Engine
#Call either the exit or the quit function.
eng1.quit()
eng2.exit()
# opt 1:
eng = matlab.engine.start_matlab("-desktop -r 'format long'")
# opt 2:
future = matlab.engine.start_matlab(async=True)
eng = future.result()

eng = eng1

eng.workspace['y']=4
eng.workspace['y2']=[24, 4, 6]
eng.workspace['y2']={24, 4, 62, 2}

eng.workspace['y3']={'ads:4','ss:5'}


# see also : https://www.mathworks.com/help/matlab/matlab_external/matlab-arrays-as-python-variables.html

A = matlab.int8([1,2,3,4,5])
print(A.size)
print eng.workspace['ans']


#https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-from-python.html
tf = eng.isprime(37)
print(tf)

t = eng.gcd(100.0,80.0,nargout=3)
print(t)

eng.doc(nargout=0)

future = eng.sqrt(4.0,async=True)
ret = future.result()
tf = future.done()
print(tf)
if tf:
    print(ret)
else:
    print "matlab not done yet"
    
#future.cancel() aborts
    
eng.edit('example_function',nargout=0)
eng.edit('example_script',nargout=0)

eng.example_script(nargout=0)
ret = eng.example_function(1.0, 2.3)
print ret

#https://www.mathworks.com/help/matlab/matlab_external/use-matlab-arrays-in-python.html
a = matlab.double([1,4,9,16,25])
b = eng.sqrt(a)
print(b)

a = eng.magic(6)
for x in a: print(x)

type(eng.workspace['res'])

#todo:
#   1. https://www.mathworks.com/help/matlab/matlab_external/sort-and-plot-matlab-data-from-python.html
#   2. https://www.mathworks.com/help/matlab/matlab_external/use-matlab-handle-objects-in-python.html 
#   3. https://www.mathworks.com/help/matlab/matlab_external/matlab-arrays-as-python-variables.html
eng.eval("T = readtable('patients.dat');",nargout=0)

#####################
#todo2:
#from matlab existing session run: matlab.engine.shareEngine
import matlab.engine
eng = matlab.engine.connect_matlab()
eng.sqrt(4.0)

matlab.engine.find_matlab()
eng.quit()
newEngine = matlab.engine.connect_matlab('MATLAB_2656')

# can run from cmd : 
# matlab -r "matlab.engine.shareEngine('MATLABEngine_for_Py')"

######################
# check:
# https://www.mathworks.com/help/matlab/matlab_external/pass-data-to-matlab-from-python.html
# https://www.mathworks.com/help/matlab/matlab_external/handle-data-returned-from-matlab-to-python.html
