from fabric.api import *

env.user = 'userName'
env.key_filename = 'Path to ssh-key file'


svrlist1 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist2 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist3 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist4 = ['IP1','IP2','IP3','IP4',  ..,'IPN']

@hosts(lab1)
def lab1tailf():
        sudo(' tail -f /var/log/messages')
@hosts(lab2)
def lab2tailf():
        sudo(' tail -f /var/log/messages')
@hosts(lab3)
def lab3tailf():
        sudo(' tail -f /var/log/messages')
@hosts(lab4)
def lab4tailf():
        sudo(' tail -f /var/log/messages')
