# ref : https://github.com/giampaolo/psutil

import psutil
import subprocess
import time

SLICE_IN_SECONDS = 1
cmd = 'C:\Program Files (x86)\Notepad++\Notepad++.exe'
p = subprocess.Popen(cmd)
pU = psutil.Process(p.pid)
resultTable = []
while p.poll() == None:
	print 'pid : pid '
	print p.pid

	for x in range(3):
		resultTable.append(psutil.cpu_percent(interval=1, percpu=True))
	
	runninfFlag = pU.is_running()
	print runninfFlag
	if runninfFlag:
		print psutil.virtual_memory()
		print psutil.swap_memory()
		print psutil.users()
	  	resultTable.append(pU.memory_full_info())
	  	print ' ------------------------ '
	  	time.sleep(SLICE_IN_SECONDS)
for line in resultTable:
	print line