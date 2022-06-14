# tail_log_fabric
Using fabric to tail on multiple remote servers logs.

I created this to monitor log files in multile servers so I dont need to remotley login to each server and do a tail -f /var/log/messages with multiple windows.
This will show all logs in one windows ( Linux only)
Pre requiste:
Python3 & fabric.

How to: Just replace your server IPs with IP1,IP2 ....
example: 
fab -P svrlist1tailf 
