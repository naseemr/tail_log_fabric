# tail_log_fabric
Using fabric to tail on multiple remote servers logs.

I created this to monitor log files in multile servers so I dont need to remotley login to each server and do a tail -f /var/log/messages with multiple windows.
This will show all logs in one windows ( inux only)
Pre requiste:
Python3 & fabric.

How to:
example: 
fab -P svrlist1tailf 
