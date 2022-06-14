from fabric.api import *

env.user = 'userName'
env.key_filename = 'Path to ssh-key file'


svrlist1 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist2 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist3 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist4 = ['IP1','IP2','IP3','IP4',  ..,'IPN']

@hosts(svrlist1)
def svrlist1tailf():
        sudo(' tail -f /var/log/messages')
@hosts(svrlist2)
def svrlist2tailf():
        sudo(' tail -f /var/log/messages')
@hosts(svrlist3)
def svrlist3tailf():
        sudo(' tail -f /var/log/messages')
@hosts(svrlist4)
def svrlist4tailf():
        sudo(' tail -f /var/log/messages')
